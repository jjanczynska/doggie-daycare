from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Owner, Dog, Reservation, Testimonial, Comment
from .forms import DogForm, ReservationForm, TestimonialForm, CommentForm


# Reservations View:


@login_required
def reservations(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            owner, created = Owner.objects.get_or_create(user=request.user)
            owner.tel_no = form.cleaned_data.get('tel_no', '')
            owner.email_address = form.cleaned_data.get('email_address', '')
            owner.save()

            dog, created = Dog.objects.get_or_create(
                owner=owner,
                name=form.cleaned_data['name'],
                defaults={
                    'gender': form.cleaned_data['gender'],
                    'breed': form.cleaned_data['breed'],
                    'food_provided': form.cleaned_data['food_provided'],
                    'vaccinations_up_to_date': 
                        form.cleaned_data['vaccinations_up_to_date']
                }
            )

            reservation = form.save(commit=False)
            reservation.owner = owner
            reservation.dog = dog
            reservation.save()

            messages.success(request, 'Reservation successfully created!')
            return redirect('reservations')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ReservationForm()

    existing_reservations = Reservation.objects.filter(
        owner__user=request.user
        )
    return render(
        request,
        'reservations.html',
        {'form': form, 'reservations': existing_reservations}
    )
