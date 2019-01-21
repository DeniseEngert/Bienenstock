from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    areas_of_interest = models.CharField(_('areas_of_interest'), max_length=100, blank=True)
    address = models.CharField(_('address'), max_length=100, blank=True)
    phone_number = models.CharField(_('phone_number'), max_length=12, blank=True)
    bio = models.CharField(_('bio'), max_length=4000, blank=True)
    birth_date = models.CharField(_('birth_date'), max_length=30, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(_('image'), upload_to='images/', default='images/None/placeUser.png')

    def uploadImage(self, filename):
        return 'post/{}/{}'.format(self.user.username, filename)

    def __str__(self):
        return self.bio


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
