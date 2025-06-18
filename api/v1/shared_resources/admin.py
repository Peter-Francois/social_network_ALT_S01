from django.contrib import admin
from .models import SharedResource


class SharedResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource_type', 'creator', 'created_at')
    list_filter = ('resource_type', 'creator')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

admin.site.register(SharedResource, SharedResourceAdmin)
