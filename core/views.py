from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage
from django.utils import timezone
from .forms import BookingForm
from .models import *
from events.models import Event
from blog.models import Post

def home(request):
    today = timezone.now().date()

    recent_posts = (
        Post.objects
        .filter(published=True)
        .order_by('-created_at')[:3]
    )

    past_events = (
        Event.objects
        .filter(date__lt=today, is_published=True)
        .order_by('-date')[:2]   # limit for homepage
    )

    return render(request, "core/home.html", {
        "recent_posts": recent_posts,
        "past_events": past_events
    })


def book_service(request):
    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            booking = form.save(commit=False)
            # Fee is already set in the form's clean method
            booking.save()
            messages.success(request, '🎉 Booking submitted successfully! We will contact you shortly to confirm.')
            return redirect('book-service')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BookingForm()
    
    context = {
        'form': form,
        'service_fees': SERVICE_FEES,
        'service_choices': SERVICE_CHOICES,
    }
    return render(request, 'core/book_service.html', context)

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )
        messages.success(request, 'Thank you for your message! We\'ll get back to you soon.')
        return redirect('home')
    
    return redirect('home')