from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'published', 'has_image')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('published', 'created_at', 'author')
    search_fields = ('title', 'content')
    
    def has_image(self, obj):
        return bool(obj.featured_image)
    has_image.boolean = True
    has_image.short_description = 'Has Image'