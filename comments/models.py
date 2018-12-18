from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

# Create your models here.
class Commentary(models.Model):
    text = models.TextField(max_length=4000)
    time = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_commentary')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_commentary')
