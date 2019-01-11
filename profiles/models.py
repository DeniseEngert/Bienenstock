from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    areas_of_interest = models.CharField(max_length=100, default='Bienen')
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profile')
