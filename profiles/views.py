from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from profiles.forms import *
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from projects.models import Project
from profiles.models import Profile as Filepro


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, u'Registrierungsdaten erfolgreich gespeichert!')
            return HttpResponseRedirect(reverse('projects'))
        else:
            messages.error(request, u'falsche Nutzerdaten.')
            pass
    else:
        form = RegistrationForm()
    return render(request, 'profiles/signup.html', {'form': form})


def ShowProfile(request):
    profiles = Profile.objects.order_by('user')
    return render(request, 'profiles/profile.html', {'profiles': profiles})


class Dashboard(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'profiles/dashboard.html', {"projects": Project.objects.all()})


class DashboardList(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'profiles/dashboard_list.html', {"projects": Project.objects.all()})


class Profile(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'profiles/profile.html', {"profile": Filepro.objects.all()})
