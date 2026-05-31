from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Product, Cart, CartItem, ProductInquiry

def shop_view(request):
    products = Product.objects.filter(in_stock=True)  # Only show in-stock products
    return render(request, 'shop/shop.html', {'products': products})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Check if product is in stock
    if not product.in_stock:
        messages.warning(request, f"{product.name} is currently out of stock.")
        return redirect('shop')
    
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f"Updated {product.name} quantity in your cart.")
    else:
        messages.success(request, f"{product.name} added to your cart.")
    
    return redirect('shop')

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    total = cart.get_total()
    return render(request, 'shop/cart.html', {'cart': cart, 'items': items, 'total': total})

@login_required
def update_cart(request, item_id):
    """Update cart item quantity"""
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 0))
        if quantity > 0:
            item.quantity = quantity
            item.save()
            messages.success(request, "Cart updated successfully.")
        else:
            item.delete()
            messages.info(request, "Item removed from cart.")
    
    return redirect('view_cart')

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    product_name = item.product.name
    item.delete()
    messages.info(request, f"{product_name} removed from cart.")
    return redirect('view_cart')

@login_required
def whatsapp_checkout(request):
    """Send cart contents via WhatsApp inquiry instead of payment"""
    cart = Cart.objects.filter(user=request.user).first()
    
    if not cart or cart.items.count() == 0:
        messages.warning(request, "Your cart is empty.")
        return redirect('view_cart')
    
    # Build WhatsApp message with cart items
    items_list = []
    for item in cart.items.all():
        items_list.append(f"• {item.product.name} x{item.quantity} = KES {item.get_subtotal()}")
    
    items_text = "\n".join(items_list)
    
    message = f"🛍️ *NEW ORDER INQUIRY*%0A%0A"
    message += f"*Customer:* {request.user.get_full_name() or request.user.username}%0A"
    message += f"*Email:* {request.user.email}%0A"
    message += f"*Phone:* {request.user.profile.phone if hasattr(request.user, 'profile') else 'Not provided'}%0A%0A"
    message += f"*Items Ordered:*%0A{items_text}%0A%0A"
    message += f"*Total:* KES {cart.get_total()}%0A%0A"
    message += f"Please contact me to arrange delivery and payment."
    
    # WhatsApp number (update with your actual number)
    whatsapp_number = "254798503335"
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={message}"
    
    # Optional: Save inquiry to database
    for item in cart.items.all():
        ProductInquiry.objects.create(
            product=item.product,
            customer_name=request.user.get_full_name() or request.user.username,
            customer_email=request.user.email,
            customer_phone=request.user.profile.phone if hasattr(request.user, 'profile') else '',
            message=f"Quantity: {item.quantity}\nTotal: KES {cart.get_total()}"
        )
    
    # Optional: Clear cart after inquiry
    # cart.items.all().delete()
    # messages.success(request, "Your inquiry has been sent! We'll contact you soon.")
    
    return redirect(whatsapp_url)

@login_required
def product_whatsapp_inquiry(request, product_id):
    """Direct WhatsApp inquiry for a single product"""
    product = get_object_or_404(Product, id=product_id)
    
    message = f"Hi! I'm interested in *{product.name}* (KES {product.price}) from The Pet People Shop."
    
    whatsapp_number = "254798503335"
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={message.replace(' ', '%20')}"
    
    return redirect(whatsapp_url)

def product_detail(request, pk):
    """View for single product detail"""
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})