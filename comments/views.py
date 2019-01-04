from django.contrib.auth.decorators import login_required
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


@login_required
def new_project_commentary(request, pk):
    project = get_object_or_404(Project, pk=pk)
    user = request.user
    # projects = Project.objects.all()
    # project = Project.objects.first()
    if request.method == 'POST':
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.project = project
            commentary.user = user
            commentary.save()
            return redirect('editProject', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'comments/new_project_commentary.html', {'project':project})
