from django.db import models
from .custom_user import CustomUser

class ServiceProviderProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField()
    skills = models.TextField(max_length=255)
    experience = models.TextField()
    per_hour_rate = models.DecimalField(max_digits=10, decimal_places=2)
