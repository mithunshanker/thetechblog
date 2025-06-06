from django.contrib import admin

from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Columns to show in admin list view
    search_fields = ('title', 'content')    # Enable search in admin for these fields
    list_filter = ('created_at',)            # Add filtering options by date

