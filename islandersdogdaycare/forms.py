from django import forms
from .models import Reservation, Testimonial, Comment


class ReservationForm(forms.ModelForm):
    # Owner Details
    tel_no = forms.CharField(label='Telephone Number', max_length=15)

    # Dog Details
    name = forms.CharField(max_length=50)
    sex = forms.ChoiceField(choices=Dog.SEX_CHOICES)
    breed = forms.CharField(max_length=50)
    food_provided = forms.BooleanField(required=False)
    vaccinations_up_to_date = forms.BooleanField(required=False)
    
    class Meta:
        model = Reservation
        fields = ['dog', 'date_of_daycare', 'tel_no']


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['title', 'excerpt', 'content', 'featured_image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
