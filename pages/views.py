from django.shortcuts import render
from .models import Page
from django.views import View
# Create your views here.

def start(request):
    return render(request, 'pages/start.html', {"pages": Page.objects.all() })

class PageView(View):
    def get(self, request, slug):
       page = Page.objects.get(slug=slug)
       return render(request, 'pages/page.html', {"page": page})
