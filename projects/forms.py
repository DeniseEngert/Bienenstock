from django.forms import *
from .models import *
from django.utils.translation import ugettext_lazy as _


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'picture', 'category', 'is_public')
        labels = {
            'is_public': _('is public'),
        }


class DatasetForm(ModelForm):
    class Meta:
        model = Dataset
        fields = {'title', 'data_file'}
