from django.db import models
from django.utils import timezone
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    location = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event_detail', args=[self.slug])

    def is_upcoming(self):
        return self.date >= timezone.now().date()
