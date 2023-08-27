from django import forms
from .models import Reservation, Testimonial, Comment


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = 'body'


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['title', 'excerpt', 'content', 'featured_image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
