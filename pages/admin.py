from django.contrib import admin
from .models import Page
from mptt.admin import DraggableMPTTAdmin

admin.site.register(Page, DraggableMPTTAdmin,
                    list_display=(
                        'tree_actions',
                        'indented_title',
                    ),
                    list_display_links=(
                        'indented_title',
                    ),
                    )
