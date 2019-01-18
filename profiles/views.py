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
from django.contrib.auth.decorators import login_required
from django.db import transaction


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


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileView(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, u'Successfully updated!')
            return HttpResponseRedirect(reverse('profile'))
        else:
            messages.error(request, u'Please correct error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileView(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


class Dashboard(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        projects = Project.objects.filter(user=request.user)
        return render(request, 'profiles/dashboard.html', {"projects": projects})


class DashboardList(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        projects = Project.objects.filter(user=request.user)
        return render(request, 'profiles/dashboard_list.html', {"projects": projects})


class Profile(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'profiles/profile.html', {"profile": Filepro.objects.all()})
