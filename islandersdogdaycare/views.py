from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Owner, Dog, Reservation, Testimonial, Comment
from .forms import DogForm, ReservationForm, TestimonialForm, CommentForm


# Reservations View:


@login_required
def reservations(request):
    form = ReservationForm
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            owner, created = Owner.objects.get_or_create(user=request.user)
            owner.tel_no = form.cleaned_data['tel_no']
            owner.email_address = form.cleaned_data['default@example.com']
            owner.save()

        dog = Dog.objects.create(
                owner=owner,
                name=form.cleaned_data['name'],
                gender=form.cleaned_data['gender'],
                breed=form.cleaned_data['breed'],
                food_provided=form.cleaned_data['food_provided'],
                vaccinations_up_to_date=form.cleaned_data
                ['vaccinations_up_to_date']
            )

        reservation = form.save(commit=False)
        reservation.owner = owner
        reservation.dog = dog
        reservation.save()

        return redirect('reservations')

    else:
        form = ReservationForm()

    existing_reservations = Reservation.objects.filter(
        owner__user=request.user)
    return render(
        request,
        'reservations.html',
        {'form': form, 'reservations': existing_reservations})
