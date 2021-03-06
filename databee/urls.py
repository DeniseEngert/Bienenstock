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

# for project sites
from projects import views as projects_views

# for comments
from comments import views as comments_views

# for serving media and static files
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

# single pages
from pages import views as pages_views

#translation
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', pages_views.StartPage.as_view(), name='start'),
    path('register/', profiles_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', profiles_views.Dashboard.as_view(), name='dashboard'),
    path('dashboard/list/', profiles_views.Dashboard.as_view(), {'view': 'list'}, name='dashboardList'),
    path('profile/', profiles_views.update_profile, name='profile'),
    path('projects/', projects_views.ProjectList.as_view(), name='projects'),
    path('project/add/', projects_views.ProjectCreate.as_view(), name="addProject"),
    path('project/<int:pk>/edit', projects_views.ProjectUpdate.as_view(), name="editProject"),
    path('project/<int:pk>/', projects_views.PublicProjectDetailView.as_view(), name="viewPublicProject"),
    path('project/<int:pk>/comment/', comments_views.CommentaryCreateView.as_view(), name='newProjectCommentary'),
    path('commentary/<int:pk>/delete/', comments_views.CommentaryDeleteView.as_view(), name='deleteProjectCommentary'),
    path('project/<int:pk>/delete/', projects_views.ProjectDelete.as_view(), name="deleteProject"),
    path('project/<int:pk>/dataset/add/', projects_views.DatasetCreate.as_view(), name="addDataset"),
    path('project/<int:project_pk>/dataset/<int:pk>/', projects_views.DatasetDetail.as_view(), name="showDataset"),
    path('project/<int:project_pk>/dataset/<int:pk>/edit/', projects_views.DatasetUpdate.as_view(), name="editDataset"),
    path('project/<int:project_pk>/dataset/<int:pk>/delete/', projects_views.DatasetDelete.as_view(), name="deleteDataset"),
    path('<str:slug>/', pages_views.PageView.as_view(), name="showPage"),
]

if not settings.ON_HEROKU:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
