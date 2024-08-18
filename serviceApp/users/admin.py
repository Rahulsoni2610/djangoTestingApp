from django.contrib import admin
from .models import CustomUser

# Register your models here.

regiter = admin.site.register

regiter(CustomUser)