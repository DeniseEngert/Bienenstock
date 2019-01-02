from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# model for basic pages
class Page(MPTTModel):
    title = models.CharField(max_length=30, blank=False, default="")
    image = models.ImageField(upload_to='images', blank=True, null=True)
    teaser = models.CharField(max_length=100, blank=True)
    text = models.TextField(max_length=4000)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title