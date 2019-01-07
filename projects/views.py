from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class ProjectList(ListView):
    model = Project
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.all().filter(is_public=True).order_by('-updated')

class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('projects')


class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "projects/project_detail.html"


class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('projects')


class DatasetCreateView(LoginRequiredMixin, CreateView):
    model = Dataset
    form_class = DatasetForm
    template_name = "projects/new_dataset.html"

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, pk=kwargs['pk'])
        return super(DatasetCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.project = self.project
        return super(DatasetCreateView, self).form_valid(form)


@login_required
def showdataset(request, pk, pk_dataset):
    dataset = get_object_or_404(Dataset, pk=pk_dataset)
    return render(request, 'projects/dataset_detail.html', {'dataset': dataset})
