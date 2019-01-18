from .models import Page


def settings(request):
    return {'pages': Page.objects.all()}
