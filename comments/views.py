from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Project
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .forms import CommentaryForm
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class CommentaryCreateView(LoginRequiredMixin,CreateView):
    model = Commentary
    template_name = 'comments/new_project_commentary.html'
    form_class = CommentaryForm
    # success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, pk=kwargs['pk'])
        return super(CommentaryCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        commentary = form.save(commit=False)
        commentary.user = self.request.user
        form.instance.project = self.project
        return super(CommentaryCreateView, self).form_valid(form)