from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from .forms import CommentaryForm
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseForbidden


class CommentaryCreateView(LoginRequiredMixin, CreateView):
    model = Commentary
    template_name = 'projects/project_detail.html'
    form_class = CommentaryForm

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, pk=kwargs['pk'])
        return super(CommentaryCreateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CommentaryCreateView, self).get_context_data(**kwargs)
        context['project'] = self.project
        context['commentaryForm'] = context.get('form')
        return context

    def form_valid(self, form):
        commentary = form.save(commit=False)
        commentary.user = self.request.user
        form.instance.project = self.project
        return super(CommentaryCreateView, self).form_valid(form)


class CommentaryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Commentary

    def has_permission(self):
        commentary = self.get_object()
        return commentary.user == self.request.user

    def dispatch(self, request, *args, **kwargs):
        comment = self.get_object()
        project = comment.project
        if project.user == request.user:
            self.success_url = reverse_lazy('editProject', kwargs={'pk': project.pk})
        else:
            self.success_url = reverse_lazy('viewPublicProject', kwargs={'pk': project.pk})
        return super(CommentaryDeleteView, self).dispatch(request, *args, **kwargs)
