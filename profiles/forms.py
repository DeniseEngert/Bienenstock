from django.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class ProfileView(ModelForm):
    class Meta:
        model = Profile
        fields = ('areas_of_interest', 'address', 'phone_number')



