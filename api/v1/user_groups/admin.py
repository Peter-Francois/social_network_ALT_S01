from django.contrib import admin
from .models import UserGroup


class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'creation_date', 'creator')
    list_filter = ('creator',)
    search_fields = ('name', 'description')
    ordering = ('-creation_date',)

admin.site.register(UserGroup, UserGroupAdmin)

