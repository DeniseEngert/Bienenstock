from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    areas_of_interest = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    bio = models.CharField(max_length=500, blank=True)
    birth_date = models.CharField(max_length=30, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
