from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Event

def event_list(request):
    today = timezone.now().date()
    upcoming_events = Event.objects.filter(date__gte=today, is_published=True).order_by('date')
    past_events = Event.objects.filter(date__lt=today, is_published=True).order_by('-date')

    return render(request, 'events/event_list.html', {
        'upcoming_events': upcoming_events,
        'past_events': past_events
    })

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug, is_published=True)
    return render(request, 'events/event_detail.html', {'event': event})
