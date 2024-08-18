from rest_framework import serializers
from .models.custom_user import CustomUser
from .models.custom_user import Location
from .models.otp import Otp
from django.contrib.auth.hashers import make_password

class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Location
    fields = ['state', 'city']


class CustomUserSerializer(serializers.ModelSerializer):
  location = LocationSerializer()

  class Meta:
    model = CustomUser
    fields = ['id','email', 'password', 'first_name', 'last_name', 'contact_no', 'address', 'role', 'location']

  def create(self, validated_data):
    validated_data['password'] = make_password(validated_data['password'])
    location_data = validated_data.pop('location')
    location, created = Location.objects.get_or_create(**location_data)
    user = CustomUser.objects.create(location=location, **validated_data)
    return user

  def update(self, instance, validated_data):
    location_data = validated_data.pop('location')
    location, created = Location.objects.get_or_create(**location_data)

    instance.location = location
    instance.email = validated_data.get('email', instance.email)
    instance.password = validated_data.get('password', instance.password)
    instance.first_name = validated_data.get('first_name', instance.first_name)
    instance.last_name = validated_data.get('last_name', instance.last_name)
    instance.contact_no = validated_data.get('contact_no', instance.contact_no)
    instance.address = validated_data.get('address', instance.address)
    instance.role = validated_data.get('role', instance.role)

    instance.save()
    return instance

class LoginSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ["email", "password"]

class OtpSerializer(serializers.ModelSerializer):
  class Meta:
      model = Otp
      # fields = ['email']
      fields = '__all__'
