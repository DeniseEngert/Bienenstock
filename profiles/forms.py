from django.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from .models import *


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', "last_name", 'email')
        labels = {
            'first_name': _('First name'),
            'last_name': _('Last name'),
        }


class ProfileView(ModelForm):
    class Meta:
        model = Profile
        fields = ('image', 'areas_of_interest', 'address', 'phone_number', 'birth_date', 'bio')
        labels = {
            'areas_of_interest': _('Areas of interest'),
            'phone_number': _('Phone number'),
            'birth_date': _('Birth date'),
        }
