from django.shortcuts import render
from .models import *
from .forms import *

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormMixin

# Create your views here.

def projects(request):
    return render(request, 'projects.html')

class ProjectList(ListView):
    model = Project
    context_object_name = 'projects'

class ProjectCreate(CreateView):
    model = Project
    form_class = ProjectForm

class ProjectUpdate(UpdateView):
    model = Project
    form_class = ProjectForm

class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('projects')
