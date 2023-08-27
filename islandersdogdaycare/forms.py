from django import forms
from .models import Reservation, Testimonial, Comment


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = 'body'

