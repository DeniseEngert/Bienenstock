from django.db import models

# Create your models here.
class Page(models.Model):
    about_text = models.TextField(max_length=4000)
