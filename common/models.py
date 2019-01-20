from django.db import models
from django.utils.translation import gettext_lazy as _

class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class SiteSettings(SingletonModel):
    support = models.EmailField()
    about_text = models.CharField(_('about_text'), max_length=4999)

    def __str__(self):
        return "Site Settings"
