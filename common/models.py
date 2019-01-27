from django.db import models
from django.utils.translation import gettext_lazy as _
from markupfield.fields import MarkupField

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
    class Meta:
        verbose_name_plural = "Site Settings"

    description = models.CharField(_('description'), max_length=300, blank=True)
    description_en = models.CharField(_('description (EN)'), max_length=300, blank=True)
    contact = models.CharField(_('contact'), max_length=300, blank=True)
    contact_en = models.CharField(_('contact (EN)'), max_length=300, blank=True)
    about_text = MarkupField(_('about_text'), markup_type='markdown', escape_html=True, blank=True)
    about_text_en = MarkupField(_('about_text (EN)'), markup_type='markdown', escape_html=True, blank=True)

    def __str__(self):
        return "Site Settings"
