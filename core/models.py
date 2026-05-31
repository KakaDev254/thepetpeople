from django.db import models
from cloudinary.models import CloudinaryField

SERVICE_CHOICES = [
    ('Boarding', 'Boarding 🏠'),
    ('Grooming', 'Grooming ✂️'),
    ('Play Time', 'Play Time 🏊‍♂️'),
    ('Meals', 'Curated Meals 🍲'),
    ('Training', 'Fitness & Training 🐕'),
    ('Massage', 'Massages & Physio'),
    ('Coffee', 'Coffee Bar ☕'),
    ('Workspace', 'Working Space 💻'),
    ('Add-ons', 'Add-ons ➕'),
]

SERVICE_FEES = {
    'Boarding': 1500,
    'Grooming': 800,
    'Play Time': 500,
    'Meals': 600,
    'Training': 1200,
    'Massage': 1000,
    'Coffee': 300,
    'Workspace': 400,
    'Add-ons': 200,
}

class Booking(models.Model):
    name = models.CharField(max_length=100)
    pet_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    fee = models.PositiveIntegerField()
    date = models.DateField()
    consent = models.BooleanField(default=False)
    pet_photo = CloudinaryField('image', folder='booking_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.service} ({self.pet_name})"
    
    def save(self, *args, **kwargs):
        if not self.fee:
            self.fee = SERVICE_FEES.get(self.service, 0)
        super().save(*args, **kwargs)


# Add the ContactMessage model
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.name} - {self.created_at}"
    
    class Meta:
        ordering = ['-created_at']