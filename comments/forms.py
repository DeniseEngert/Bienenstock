from django.forms import *
from .models import *


class CommentaryForm(ModelForm):
    class Meta:
        model = Commentary
        fields = ('text',)
