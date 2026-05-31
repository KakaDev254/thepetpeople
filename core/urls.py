from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("booking/", views.book_service, name="book-service"),
    path('contact/',views.contact_view, name='contact'),
]
