from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'published')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('published', 'created_at', 'author')
    search_fields = ('title', 'content')