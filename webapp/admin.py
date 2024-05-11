from django.contrib import admin
from webapp.models import GuestBook


@admin.register(GuestBook)
class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'author_name', 'created_at']
    list_filter = ['author_name']
    search_fields = ['id', 'author_name']
    fields = ['author_name', 'author_gmail', 'text', 'status', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
