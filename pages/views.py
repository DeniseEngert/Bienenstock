from django.shortcuts import render
from .models import Page
from projects.models import Project
from django.views import View
# Create your views here.

def start(request):
    return render(request, 'pages/start.html', {
        "pages": Page.objects.all(),
        "projects": Project.objects.all().filter(is_public=True).order_by('-updated')[:3]
    })

class PageView(View):
    def get(self, request, slug):
       page = Page.objects.get(slug=slug)
       return render(request, 'pages/page.html', {"page": page})
