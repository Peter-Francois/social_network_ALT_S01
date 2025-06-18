from django.contrib import admin
from .models import Publication


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'publication_date')
    list_filter = ('user', 'publication_date')
    search_fields = ('content',)
    ordering = ('-publication_date',)

admin.site.register(Publication, PublicationAdmin)
