from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from profiles.forms import *

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
    return render(request, 'register.html', {'form': form})
