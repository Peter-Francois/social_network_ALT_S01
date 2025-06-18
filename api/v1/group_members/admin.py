from django.contrib import admin
from .models import GroupMember


class GroupMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'group', 'join_date', 'member_status', 'member_role')
    list_filter = ('group', 'member_status', 'member_role')
    search_fields = ('user__username', 'group__name')
    ordering = ('-join_date',)

admin.site.register(GroupMember, GroupMemberAdmin)
