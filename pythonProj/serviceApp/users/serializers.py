from rest_framework import serializers
from .models import User
from .models import Location
import pdb

class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Location
    fields = ['state', 'city']


class UserSerializer(serializers.ModelSerializer):
  location = LocationSerializer(source='location_id')

  class Meta:
    model = User
    fields = ['id','email', 'password', 'first_name', 'last_name', 'contact_no', 'address_line_1', 'role', 'location']

  def create(self, validated_data):
    location_data = validated_data.pop('location_id')
    location, created = Location.objects.get_or_create(**location_data)
    user = User.objects.create(location_id=location, **validated_data)
    return user

  def update(self, instance, validated_data):
    pdb.set_trace()
    location_data = validated_data.pop('location_id')
    location, created = Location.objects.get_or_create(**location_data)

    instance.location_id = location
    instance.email = validated_data.get('email', instance.email)
    instance.password = validated_data.get('password', instance.password)
    instance.first_name = validated_data.get('first_name', instance.first_name)
    instance.last_name = validated_data.get('last_name', instance.last_name)
    instance.contact_no = validated_data.get('contact_no', instance.contact_no)
    instance.address_line_1 = validated_data.get('address_line_1', instance.address_line_1)
    instance.role = validated_data.get('role', instance.role)

    instance.save()
    return instance

