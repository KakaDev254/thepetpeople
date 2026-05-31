from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_view, name='shop'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/whatsapp/', views.whatsapp_checkout, name='whatsapp_checkout'),
    path('inquiry/<int:product_id>/', views.product_whatsapp_inquiry, name='product_whatsapp_inquiry'),
]