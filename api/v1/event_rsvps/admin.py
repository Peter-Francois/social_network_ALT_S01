from django.contrib import admin
from .models import EventRSVP


class EventRSVPAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'status', 'response_date')
    list_filter = ('status', 'response_date')
    search_fields = ('user__username', 'event__name')

admin.site.register(EventRSVP, EventRSVPAdmin)
