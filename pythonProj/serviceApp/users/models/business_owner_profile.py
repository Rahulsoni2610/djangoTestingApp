from  django.db import models
from  .custom_user import CustomUser
class BusinessOwnerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
