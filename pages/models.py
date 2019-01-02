from django.db import models

# model for basic pages
class Page(models.Model):
    title = models.CharField(max_length=30, blank=False, default="")
    image = models.ImageField(upload_to='images', null=True)
    teaser = models.CharField(max_length=100, blank=True)
    text = models.TextField(max_length=4000)
