from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm
from .models import SERVICE_FEES

def home(request):
    return render(request, "core/home.html")


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