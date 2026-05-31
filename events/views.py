from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Event

def event_list(request):
    today = timezone.now().date()
    upcoming_events = Event.objects.filter(date__gte=today, is_published=True).order_by('date')
    past_events = Event.objects.filter(date__lt=today, is_published=True).order_by('-date')

    context = {
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'has_upcoming': upcoming_events.exists(),
        'has_past': past_events.exists(),
    }
    
    return render(request, 'events/event_list.html', context)

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug, is_published=True)
    
    # Get next and previous events for navigation
    today = timezone.now().date()
    next_event = Event.objects.filter(
        date__gte=today, 
        is_published=True,
        date__gt=event.date
    ).order_by('date').first()
    
    prev_event = Event.objects.filter(
        is_published=True,
        date__lt=event.date
    ).order_by('-date').first()
    
    context = {
        'event': event,
        'next_event': next_event,
        'prev_event': prev_event,
    }
    
    return render(request, 'events/event_detail.html', context)