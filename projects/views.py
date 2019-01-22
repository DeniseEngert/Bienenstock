from django.shortcuts import get_object_or_404
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from comments.forms import CommentaryForm


class ProjectList(ListView):
    model = Project
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.all().filter(is_public=True).order_by('-updated')


class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        project = form.save(commit=False)
        project.user = self.request.user
        return super(ProjectCreate, self).form_valid(form)


class ProjectUpdate(PermissionRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "projects/project_detail.html"

    def has_permission(self):
        project = self.get_object()
        return project.user == self.request.user

    def get_context_data(self, **kwargs):
        context = super(ProjectUpdate, self).get_context_data(**kwargs)
        context['commentaryForm'] = CommentaryForm()
        return context


class PublicProjectDetailView(PermissionRequiredMixin, DetailView):
    model = Project
    template_name = "projects/public_project_detail.html"

    def get_context_data(self, **kwargs):
        context = super(PublicProjectDetailView, self).get_context_data(**kwargs)
        context['commentaryForm'] = CommentaryForm()
        return context

    def has_permission(self):
        project = self.get_object()
        return project.is_public


class ProjectDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('dashboard')

    def has_permission(self):
        project = self.get_object()
        return project.user == self.request.user


class DatasetCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Dataset
    form_class = DatasetForm

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, pk=kwargs['pk'])
        return super(DatasetCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.project = self.project
        return super(DatasetCreate, self).form_valid(form)

    def has_permission(self):
        project = self.project
        return project.user == self.request.user


class DatasetDetail(PermissionRequiredMixin, DetailView):
    model = Dataset
    template_name = 'projects/dataset_detail.html'

    def has_permission(self):
        project = self.get_object().project
        return project.user == self.request.user or project.is_public


class DatasetUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Dataset
    form_class = DatasetForm

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, pk=kwargs['project_pk'])
        return super(DatasetUpdate, self).dispatch(request, *args, **kwargs)

    def has_permission(self):
        dataset = self.get_object()
        return dataset.project.user == self.request.user

    def get_context_data(self, **kwargs):
        context = super(DatasetUpdate, self).get_context_data(**kwargs)
        context['commentaryForm'] = CommentaryForm()
        return context


class DatasetDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Dataset

    def has_permission(self):
        dataset = self.get_object()
        return dataset.project.user == self.request.user

    def get_success_url(self):
        dataset = self.get_object()
        return reverse_lazy('editProject', kwargs={'pk': dataset.project.pk})
