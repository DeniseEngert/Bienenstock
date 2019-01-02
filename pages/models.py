from django.db import models

# model for basic pages
class Page(models.Model):
    text = models.TextField(max_length=4000)
