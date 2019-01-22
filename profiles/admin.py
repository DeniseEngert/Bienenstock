from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin


class ProfileInline(admin.StackedInline):
    model = Profile
    max_num = 1
    extra = 0


class InlineUserAdmin(AuthUserAdmin):
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, InlineUserAdmin)
