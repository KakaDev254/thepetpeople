from django.contrib import admin
from .models import Product, Cart, CartItem, ProductInquiry

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'in_stock', 'stock_quantity', 'created_at', 'image_preview')
    list_filter = ('in_stock', 'created_at')
    search_fields = ('name', 'description')
    list_editable = ('price', 'in_stock', 'stock_quantity')
    list_per_page = 25
    
    def image_preview(self, obj):
        if obj.image:
            from django.utils.html import format_html
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 4px; object-fit: cover;" />', obj.image.url)
        return "No image"
    image_preview.short_description = 'Preview'


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'total_items', 'total_amount')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('created_at', 'updated_at')
    
    def total_items(self, obj):
        return obj.get_total_items()
    total_items.short_description = 'Total Items'
    
    def total_amount(self, obj):
        return f"KES {obj.get_total()}"
    total_amount.short_description = 'Total Amount'


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'subtotal')
    list_filter = ('cart__user',)
    search_fields = ('product__name', 'cart__user__username')
    
    def subtotal(self, obj):
        return f"KES {obj.get_subtotal()}"
    subtotal.short_description = 'Subtotal'


@admin.register(ProductInquiry)
class ProductInquiryAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer_name', 'customer_phone', 'created_at')
    list_filter = ('created_at', 'product')
    search_fields = ('customer_name', 'customer_email', 'customer_phone')
    readonly_fields = ('created_at',)