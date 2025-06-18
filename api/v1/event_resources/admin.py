from django.contrib import admin
from .models import EventResource



class EventResourceAdmin(admin.ModelAdmin):
    list_display = ('event', 'resource', 'created_at', 'updated_at')
    list_filter = ('event', 'resource', 'created_at', 'updated_at')
    search_fields = ('event__name', 'resource__name')
    ordering = ('-created_at',)

admin.site.register(EventResource)
