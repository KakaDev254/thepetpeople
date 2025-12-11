from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'pet_name', 'service', 'fee', 'date', 'consent')
    list_filter = ('service', 'date')
    search_fields = ('name', 'pet_name', 'email', 'phone')