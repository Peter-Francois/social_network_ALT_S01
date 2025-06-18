from django.contrib import admin
from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'type', 'title', 'read', 'created_at')
    list_filter = ('read', 'created_at')
    search_fields = ('recipient__username', 'title')
    ordering = ('-created_at',)

admin.site.register(Notification, NotificationAdmin)

