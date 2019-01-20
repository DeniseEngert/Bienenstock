from django.db import models
from django.contrib.auth.models import User
from projects.models import Project
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Commentary(models.Model):
    text = models.TextField(_('text'), max_length=4000)
    time = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_commentary')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_commentary')

    def get_absolute_url(self):
        if self.project.user == self.user:
            return reverse('editProject', kwargs={'pk': self.project.pk})
        else:
            return reverse('viewPublicProject', kwargs={'pk': self.project.pk})

    def __str__(self):
        return self.text
