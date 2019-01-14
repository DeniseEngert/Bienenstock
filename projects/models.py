from django.db import models
from django.urls import reverse
from .validators import validate_csv
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=30, unique=True)
    picture_platzhalter = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    is_public = models.BooleanField()
    updated = models.DateTimeField(default=timezone.now)
    tags = models.CharField(max_length=30)
    category = models.CharField(max_length=30, default="Nature")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')

    def get_absolute_url(self):
        return reverse('editProject', kwargs={'pk': self.pk})

class Dataset(models.Model):
    title = models.CharField(max_length=30, unique=True)
    data_file_link = models.URLField()
    data_file = models.FileField(upload_to='csv/', blank=False, null=True, validators=[validate_csv])
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_dataset')

    def get_absolute_url(self):
        return reverse('editProject', kwargs={'pk': self.project.pk})


# class SeriesOfMeasurement(models.Model):
    #title = models.CharField(max_length=30)
    #dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name='dataset_series')
