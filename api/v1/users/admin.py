from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'firstname', 'lastname', 'birthdate', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('email', 'firstname', 'lastname')
    ordering = ('-id',)

admin.site.register(User, UserAdmin)