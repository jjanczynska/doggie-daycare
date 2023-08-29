from django import forms
from .models import Owner, Dog, Reservation, Testimonial, Comment

# Forms for Reservation:


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Ownerfields = ('name', 'tel_no', 'email_address')


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = (
            'name',
            'breed',
            'gender',
            'vaccinations_up_to_date',
            'food_provided',
            )


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('date_of_daycare', 'notes')

# Forms for Testimonials and comments:


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['title', 'excerpt', 'content', 'featured_image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
