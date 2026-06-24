from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.booking_form, name='booking_form'),
    path('booking-success/', views.booking_success, name='booking_success'),
    path('contact/', views.contact_view, name='contact'),
]