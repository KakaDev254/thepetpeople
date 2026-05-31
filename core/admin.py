from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'pet_name', 'service', 'fee', 'date', 'consent', 'has_photo')
    list_filter = ('service', 'date', 'consent')
    search_fields = ('name', 'pet_name', 'email', 'phone')
    list_editable = ('consent',)  # Quick edit consent from list view
    readonly_fields = ('fee',)  # Make fee read-only since it's auto-calculated
    
    def has_photo(self, obj):
        # Only works if you added pet_photo field
        return bool(getattr(obj, 'pet_photo', None))
    has_photo.boolean = True
    has_photo.short_description = 'Has Photo'