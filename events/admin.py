from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'is_published', 'created_at', 'has_image')
    list_filter = ('is_published', 'date', 'created_at')
    search_fields = ('title', 'description', 'location')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-date',)
    list_editable = ('is_published',)
    list_per_page = 25
    date_hierarchy = 'date'
    
    # Add a custom method to show if event has an image
    def has_image(self, obj):
        return bool(obj.image)
    has_image.boolean = True
    has_image.short_description = 'Has Image'
    
    # Optional: Add a preview of the image in admin
    def image_preview(self, obj):
        if obj.image:
            from django.utils.html import format_html
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px; border-radius: 4px;" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Image Preview'
    
    # Add image_preview to list_display if desired
    # list_display = ('title', 'date', 'image_preview', 'location', 'is_published', 'created_at', 'has_image')
    
    # Add fieldsets for better organization
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'date', 'location')
        }),
        ('Content', {
            'fields': ('description', 'image'),
            'classes': ('wide',)
        }),
        ('Publication', {
            'fields': ('is_published',),
            'classes': ('collapse',)
        }),
    )