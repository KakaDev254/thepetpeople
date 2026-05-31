from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # Changed to CloudinaryField
    image = CloudinaryField('image', folder='shop/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Optional: Add stock tracking
    in_stock = models.BooleanField(default=True)
    stock_quantity = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    
    def get_whatsapp_message(self):
        """Generate WhatsApp message for this product"""
        return f"Hi! I'm interested in {self.name} (KES {self.price}) from The Pet People Shop."


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_total(self):
        return sum(item.get_subtotal() for item in self.items.all())

    def get_total_items(self):
        return sum(item.quantity for item in self.items.all())

    def __str__(self):
        return f"Cart ({self.user.username})"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"


# Optional: Add Inquiry model to track customer inquiries
class ProductInquiry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inquiries')
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Inquiry for {self.product.name} from {self.customer_name}"