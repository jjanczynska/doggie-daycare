from django import forms
from .models import Owner, Dog, Reservation, Testimonial, Comment

# Forms for Reservation:


class DogForm(form.ModelForm):

    class Meta:
        model = Dog
        fields = (
            'name',
            'breed',
            'gender',
            'vaccinated',
            'own_food',
            'comments'
            )


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('dog', 'date', 'notes')

# Forms for Testimonials and comments:


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['title', 'excerpt', 'content', 'featured_image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
