from django.contrib import admin
from .models import ResourceAccess


class ResourceAccessAdmin(admin.ModelAdmin):
    list_display = ('user', 'access_type', 'resource', 'granted_at', 'expires_at')
    list_filter = ('access_type', 'granted_at', 'expires_at')
    search_fields = ('user__username', 'resource__title')
    ordering = ('-granted_at',)

admin.site.register(ResourceAccess, ResourceAccessAdmin)

