from django.contrib import admin
from .models import Project, Dataset
from comments.models import Commentary


class DatasetInline(admin.StackedInline):
    model = Dataset
    extra = 0

class CommentaryInline(admin.StackedInline):
    model = Commentary
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    inlines = [DatasetInline, CommentaryInline]

admin.site.register(Project, ProjectAdmin)
