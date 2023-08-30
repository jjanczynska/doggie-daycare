from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Owner, Dog, Reservation, Testimonial, Comment

# Forms for Reservation:


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('name', 'tel_no', 'email_address')


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

        widgets = {
            'vaccinations_up_to_date': forms.RadioSelect,
            'food_provided': forms.RadioSelect
        }


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        date_of_daycare = dateField(widget=AdminDateWidget)
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
