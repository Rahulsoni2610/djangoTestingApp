from rest_framework import serializers
from .models.custom_user import CustomUser
from .models.otp import Otp
from django.contrib.auth.hashers import make_password

class CustomUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = '__all__'

  def create(self, validated_data):
    validated_data['password'] = make_password(validated_data['password'])
    return super().create(validated_data)

class LoginSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ["email", "password"]

class OtpSerializer(serializers.ModelSerializer):
  class Meta:
      model = Otp
      # fields = ['email']
      fields = '__all__'
