from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .forms import BookingForm
from .models import SERVICE_FEES
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
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Ensure fee matches the selected service
            service = form.cleaned_data['service']
            form.instance.fee = SERVICE_FEES.get(service, 0)
            form.save()
            return redirect('home')  # or a 'thank you' page
    return render(request, 'core/booking.html', {'form': form, 'service_fees': SERVICE_FEES})