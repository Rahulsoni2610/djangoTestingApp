# from django.db import models

# # class Location(models.Model):
# #   state = models.CharField(max_length=50)
# #   city = models.CharField(max_length=50)

# class User(models.Model):
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=20)
#     first_name = models.CharField(max_length=25)
#     last_name = models.CharField(max_length=25)
#     # location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
#     contact_no = models.CharField(max_length=15, null=True, blank=True)
#     address = models.CharField(max_length=100, null=True, blank=True)
#     ROLE_CHOICES = [
#         ('business_owner', 'Business Owner'),
#         ('service_provider', 'Service Provider'),
#         ('admin', 'Admin'),
#     ]
#     role = models.CharField(max_length=20, choices=ROLE_CHOICES)

#     @property

#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"

# class BusinessOwnerProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     company_name = models.CharField(max_length=255)
#     industry = models.CharField(max_length=255)

# class ServiceProviderProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField()
#     skills = models.TextField(max_length=255)
#     experience = models.TextField()
#     per_hour_rate = models.DecimalField(max_digits=10, decimal_places=2)

# class Otp(models.Model):
#     email = models.EmailField(unique=True)

