from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Product, Cart, CartItem

def shop_view(request):
    products = Product.objects.all()
    return render(request, 'shop/shop.html', {'products': products})



def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f"{product.name} added to your cart.")
    return redirect('shop')



def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    total = cart.get_total()
    return render(request, 'shop/cart.html', {'cart': cart, 'items': items, 'total': total})



def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    messages.info(request, "Item removed from cart.")
    return redirect('view_cart')


def checkout_view(request):
    cart = Cart.objects.filter(user=request.user).first()

    if not cart or cart.items.count() == 0:
        messages.warning(request, "Your cart is empty.")
        return redirect('view_cart')

    if request.method == "POST":
        # You could later connect this to payments (e.g., M-Pesa, Stripe, etc.)
        total = cart.get_total()

        # Simulate order completion
        messages.success(request, f"Order placed successfully! Total: ${total}")
        cart.items.all().delete()  # Empty the cart after checkout
        return redirect('shop')

    total = cart.get_total()
    return render(request, 'shop/checkout.html', {'cart': cart, 'total': total})