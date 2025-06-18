from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'group', 'send_date', 'content')
    list_filter = ('group',)
    search_fields = ('user__username', 'group__name')
    ordering = ('-send_date',)

admin.site.register(Message, MessageAdmin)
