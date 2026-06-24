# Django core imports
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.http import FileResponse
import os
# Third-party imports
import json
from datetime import datetime

# Local application imports
from .models import ContactMessage
from .forms import BookingForm 
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
        .order_by('-date')[:2]
    )

    return render(request, "core/home.html", {
        "recent_posts": recent_posts,
        "past_events": past_events
    })


def booking_form(request):
    if request.method == 'POST':
        # Get form data
        owner_name = request.POST.get('owner_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        emergency_contact_name = request.POST.get('emergency_contact_name')
        emergency_contact_phone = request.POST.get('emergency_contact_phone')
        
        pet_name = request.POST.get('pet_name')
        pet_type = request.POST.get('pet_type')
        breed = request.POST.get('breed')
        sex = request.POST.get('sex')
        microchipped = request.POST.get('microchipped')
        microchip_number = request.POST.get('microchip_number')
        color = request.POST.get('color')
        age = request.POST.get('age')
        sterilized = request.POST.get('sterilized')
        
        check_in_date = request.POST.get('check_in_date')
        check_out_date = request.POST.get('check_out_date')
        drop_off_time = request.POST.get('drop_off_time')
        pick_up_time = request.POST.get('pick_up_time')
        
        items_left = request.POST.getlist('items_left')
        items_left_text = ', '.join(items_left)
        other_items = request.POST.get('other_items')
        
        vaccination_proof = request.POST.get('vaccination_proof')
        rabies_vaccine = request.POST.get('rabies_vaccine')
        dhlp_vaccine = request.POST.get('dhlp_vaccine')
        deworming = request.POST.get('deworming')
        flea_tick = request.POST.get('flea_tick')
        
        vet_clinic = request.POST.get('vet_clinic')
        vet_name = request.POST.get('vet_name')
        vet_phone = request.POST.get('vet_phone')
        
        on_medication = request.POST.get('on_medication')
        medication_name = request.POST.get('medication_name')
        dosage = request.POST.get('dosage')
        admin_instructions = request.POST.get('admin_instructions')
        
        food_type = request.POST.get('food_type')
        feeding_schedule = request.POST.get('feeding_schedule')
        portion_size = request.POST.get('portion_size')
        special_diet = request.POST.get('special_diet')
        
        behaviors = request.POST.getlist('behaviors')
        behaviors_text = ', '.join(behaviors)
        behavior_notes = request.POST.get('behavior_notes')
        
        services = request.POST.getlist('services')
        services_text = ', '.join(services)
        other_requests = request.POST.get('other_requests')
        
        terms_agreed = request.POST.get('terms_agreed')
        
        # Build email content
        email_body = f"""
THE PET PEOPLE - NEW BOARDING REQUEST

OWNER DETAILS
-------------
Owner Name: {owner_name}
Phone: {phone}
Email: {email}
Address: {address}
Emergency Contact: {emergency_contact_name}
Emergency Phone: {emergency_contact_phone}

PET INFORMATION
---------------
Pet Name: {pet_name}
Pet Type: {pet_type}
Breed: {breed}
Sex: {sex}
Microchipped: {microchipped}
Microchip Number: {microchip_number}
Color/Markings: {color}
Age: {age}
Sterilized: {sterilized}

BOARDING DETAILS
----------------
Check-in Date: {check_in_date}
Check-out Date: {check_out_date}
Drop-off Time: {drop_off_time}
Pick-up Time: {pick_up_time}

ITEMS LEFT WITH PET
-------------------
{items_left_text}
Other Items: {other_items}

VACCINATION REQUIREMENTS
------------------------
Proof of Vaccination: {vaccination_proof}
Rabies Vaccine: {rabies_vaccine}
DHLP Vaccine: {dhlp_vaccine}
Deworming: {deworming}
Flea/Tick Prevention: {flea_tick}

VETERINARIAN INFORMATION
------------------------
Clinic: {vet_clinic}
Vet Name: {vet_name}
Phone: {vet_phone}

MEDICATION
----------
On Medication: {on_medication}
Medication Name: {medication_name}
Dosage: {dosage}
Instructions: {admin_instructions}

FEEDING INSTRUCTIONS
--------------------
Food Type: {food_type}
Feeding Schedule: {feeding_schedule}
Portion Size: {portion_size}
Special Diet: {special_diet}

BEHAVIORAL INFORMATION
----------------------
Behaviors: {behaviors_text}
Additional Notes: {behavior_notes}

ADDITIONAL SERVICES
-------------------
{services_text}
Other Requests: {other_requests}

TERMS & CONDITIONS
------------------
Agreed: {terms_agreed}

--- 
This booking request was submitted via The Pet People website.
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """

        # Send email to admin
        try:
            send_mail(
                subject=f'New Booking Request - {pet_name} ({owner_name})',
                message=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['info@thepetpeople.co.ke'],
                fail_silently=False,
            )
            messages.success(request, '🎉 Your booking request has been sent! We will contact you shortly.')
            return redirect('booking_success')
        except Exception as e:
            messages.error(request, f'Error sending booking request: {str(e)}')
            return redirect('booking_form')
    
    return render(request, 'core/booking_form.html')


def booking_success(request):
    return render(request, 'core/booking_success.html')


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

def download_pdf(request):
    pdf_path = os.path.join(settings.BASE_DIR, 'static', 'pdf', 'boarding_form.pdf')
    
    if os.path.exists(pdf_path):
        return FileResponse(
            open(pdf_path, 'rb'),
            content_type='application/pdf',
            filename='boarding_form.pdf'
        )
    else:
        messages.error(request, 'The boarding form PDF is currently unavailable. Please contact us directly.')
        return redirect('booking_form')