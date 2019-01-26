from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.template.defaultfilters import slugify
from markupfield.fields import MarkupField
from django.utils.translation import gettext_lazy as _


class Page(MPTTModel):
    title = models.CharField(_('title'), max_length=30, blank=False, default="")
    image = models.ImageField(_('image'), upload_to='images', blank=True, null=True)
    teaser = models.CharField(_('teaser'), max_length=100, blank=True)
    text = MarkupField(_('text'), markup_type='markdown', escape_html=True)
    slug = models.SlugField(_('slug'), max_length=60, blank=True, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def save(self, *args, **kwargs):
        if not self.id or self.slug == '':
            self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title
