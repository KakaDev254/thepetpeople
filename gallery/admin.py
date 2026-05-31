from django.contrib import admin
from .models import GalleryImage

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'image_preview')
    list_filter = ('uploaded_at',)
    search_fields = ('title', 'description')
    readonly_fields = ('uploaded_at',)
    list_per_page = 25
    
    # Add image preview in list view
    def image_preview(self, obj):
        if obj.image:
            from django.utils.html import format_html
            # For Cloudinary
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px; border-radius: 4px; object-fit: cover;" />', obj.image.url)
        return "No image"
    image_preview.short_description = 'Preview'
    
    # Optional: Add thumbnail in detail view
    fieldsets = (
        ('Image Information', {
            'fields': ('title', 'image', 'description')
        }),
        ('Metadata', {
            'fields': ('uploaded_at',),
            'classes': ('collapse',)
        }),
    )