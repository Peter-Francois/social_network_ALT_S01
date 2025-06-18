from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'location', 'location_type', 'max_participants', 'is_private', 'status', 'group')
    list_filter = ('status', 'is_private', 'location_type', 'group')
    search_fields = ('title', 'description')
    ordering = ('-start_date',)

admin.site.register(Event, EventAdmin)

