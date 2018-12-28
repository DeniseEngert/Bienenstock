"""databee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

# for user management (registration, profiles and login)
from profiles import views as profiles_views
from django.contrib.auth import views as auth_views

# project sites (private and public or just one site ???)
from projects import views as projects_views

# for serving media and static files
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

# only for hello world test
from django.http import HttpResponse
from django.template import loader


def hello_world(req):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world),
    path('register/', profiles_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('projects/', projects_views.projects, name='projects')
]

if not settings.ON_HEROKU:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
