from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'pet_name', 'email', 'phone', 'service', 'date', 'consent']
        # Removed 'fee' since it's auto-calculated
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'consent': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'pet_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Pet's Name"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your@email.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'service': forms.Select(attrs={'class': 'form-select', 'id': 'service-select'}),
        }
        labels = {
            'name': 'Your Name',
            'pet_name': "Pet's Name",
            'email': 'Email Address',
            'phone': 'Phone Number',
            'service': 'Select Service',
            'date': 'Preferred Date',
            'consent': 'I agree to the terms and conditions',
        }
        help_texts = {
            'date': 'Please select your preferred date for the service',
            'consent': 'We will contact you to confirm your booking',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make date field required
        self.fields['date'].required = True
        # Add a dynamic fee display (optional)
        self.fields['service'].widget.attrs.update({
            'onchange': 'updateFee(this.value)'
        })