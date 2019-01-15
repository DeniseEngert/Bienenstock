from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from pages.models import Page
from projects.models import Project


class StartPage(TemplateView):
    template_name = 'pages/start.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = Page.objects.all()
        context['projects'] = Project.objects.all().filter(is_public=True).order_by('-updated')[:3]
        return context


class PageView(DetailView):
    model = Page
