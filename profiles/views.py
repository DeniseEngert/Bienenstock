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
from django.views.generic import ListView


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


class Dashboard(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'profiles/dashboard.html'

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        if self.kwargs and self.kwargs['view'] == 'list':
            self.template_name = 'profiles/dashboard_list.html'
        return super(Dashboard, self).dispatch(request, *args, **kwargs)


class Profile(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'profiles/profile.html', {"profile": Filepro.objects.all()})
