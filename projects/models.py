from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30, unique=True)
    picture_platzhalter = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    is_public = models.BooleanField()
    tags = models.CharField(max_length=30)

class Dataset(models.Model):
    title = models.CharField(max_length=30, unique=True)
    data_file_link = models.URLField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_dataset')


class SeriesOfMeasurement(models.Model):
    title = models.CharField(max_length=30)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name='dataset_series')
