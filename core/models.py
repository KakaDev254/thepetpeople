from django.db import models

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

    def __str__(self):
        return f"{self.name} - {self.service} ({self.pet_name})"
