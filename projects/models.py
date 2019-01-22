from django.db import models
from django.urls import reverse
from .validators import validate_csv
from django.utils import timezone
from django.contrib.auth.models import User
from markupfield.fields import MarkupField
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    title = models.CharField(_('title'), max_length=30, unique=True)
    picture = models.ImageField(upload_to='images/', default='images/None/placeProject.png')
    description = MarkupField(_('description'), markup_type='markdown', escape_html=True)
    is_public = models.BooleanField(_('is_public'))
    updated = models.DateTimeField(default=timezone.now)
    category = models.CharField(_('category'), max_length=30, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user', related_name='creator')

    def get_absolute_url(self):
        return reverse('editProject', kwargs={'pk': self.pk})

    def __str__(self):
        return "{} / {}".format(self.user.username, self.title)


class Dataset(models.Model):
    title = models.CharField(_('title'), max_length=30, unique=True)
    data_file = models.FileField(_('data_file'), upload_to='csv/', blank=False, null=True, validators=[validate_csv])
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_dataset')

    def get_absolute_url(self):
        if self.project.user == self.user:
            return reverse('editProject', kwargs={'pk': self.project.pk})
        else:
            return reverse('viewPublicProject', kwargs={'pk': self.project.pk})

    def __str__(self):
        return "{} / {} / {}".format(self.project.user.username, self.project.title, self.title)




