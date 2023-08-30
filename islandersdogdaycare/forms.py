from django import forms
from django.forms import DateInput
from django.contrib.admin.widgets import AdminDateWidget
from .models import Owner, Dog, Reservation, Testimonial, Comment

# Forms for Reservation:


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('name', 'tel_no', 'email_address')


class DogForm(forms.ModelForm):
    vaccinations_up_to_date = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=[(True, 'Yes'), (False, 'No')],
        initial=None,
        required=False,
        label='Is your dog up to date with all required vaccinations?',
        help_text='Proof of recent vaccinations required at drop off'
    )

    food_provided = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=[(True, 'Yes'), (False, 'No')],
        initial=None,
        required=False,
        label='Are you bringing your own brand of food for your dog?',
        help_text='We can provide our own if your answer is "No"'
    )

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
    date_of_daycare = forms.DateField(
        widget=DateInput(attrs={'type': 'date'})
    )

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
