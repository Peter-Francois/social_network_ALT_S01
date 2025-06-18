from django.contrib import admin
from .models import Friendship


class FriendshipAdmin(admin.ModelAdmin):
    list_display = ('user1', 'user2', 'creation_date')
    list_filter = ('user1', 'user2')
    search_fields = ('user1__email', 'user2__email')
    ordering = ('user1', 'user2')

admin.site.register(Friendship, FriendshipAdmin)
