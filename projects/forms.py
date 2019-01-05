from django.forms import *
from .models import *


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'is_public')


class DatasetForm(ModelForm):
    class Meta:
        model = Dataset
        fields = {'title', 'data_file_link'}
