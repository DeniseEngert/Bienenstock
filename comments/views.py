from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Project
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView
from .forms import CommentaryForm
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
# Create your views here.


class CommentaryCreateView(LoginRequiredMixin,CreateView):
    model = Commentary
    template_name = 'projects/project_detail.html'
    form_class = CommentaryForm

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.project
        context['commentaryForm'] = context.get('form')
        return context

    def form_valid(self, form):
        commentary = form.save(commit=False)
        commentary.user = self.request.user
        form.instance.project = self.project
        return super(CommentaryCreateView, self).form_valid(form)


class CommentaryDeleteView(LoginRequiredMixin, DeleteView):
    model = Commentary

    def dispatch(self, request, *args, **kwargs):
        comment = self.get_object()
        project = comment.project

        # check, if user is either project owner or comment author
        if not (request.user.id == project.user.id or request.user.id == comment.user.id):
            return HttpResponseForbidden("It is not yours ! You are not permitted !")

        if project.user == request.user:
            self.success_url = reverse_lazy('editProject', kwargs={'pk': project.pk})
        else:
            self.success_url = reverse_lazy('viewPublicProject', kwargs={'pk': project.pk})
        return super(CommentaryDeleteView, self).dispatch(request, *args, **kwargs)


