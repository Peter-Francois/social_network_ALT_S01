from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'publication', 'content', 'comment_date')
    list_filter = ('user', 'publication', 'comment_date')
    search_fields = ('content',)
    ordering = ('-comment_date',)

admin.site.register(Comment, CommentAdmin)
