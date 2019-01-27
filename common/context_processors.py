from .models import SiteSettings

def settings(request):
    return {'settings': SiteSettings.load()}

def lang_context_processor(request):
    return {'lang': request.LANGUAGE_CODE}