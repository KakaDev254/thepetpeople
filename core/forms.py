from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'pet_name', 'email', 'phone', 'service', 'fee', 'date', 'consent']
        widgets = {
            'fee': forms.NumberInput(attrs={'readonly': True}),
            'consent': forms.CheckboxInput(),
        }
