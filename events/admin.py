# events/admin.py
from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'is_published', 'created_at')
    list_filter = ('is_published', 'date', 'created_at')
    search_fields = ('title', 'description', 'location')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-date',)
    list_editable = ('is_published',)
