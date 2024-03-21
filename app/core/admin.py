"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models
from .models import AudioFile


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'name']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (
            _('Important dates'),
            {
                'fields': (
                    'last_login',
                )
            }
        ),
    )
    readonly_fields = ['last_login']

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',

            )
        }),
    )
# last changes

# Register your models here.
class AudioFile(admin.ModelAdmin):
    # Define the list of fields to display in the admin list view
    list_display = ('id', 'file', 'created_at')

    # Make the 'created_at' field clickable for sorting
    list_display_links = ('created_at',)

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Recipe)
admin.site.register(models.AudioFile)
