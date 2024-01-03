from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Owner, Dog, Reservation, Testimonial, Comment
from django.urls import reverse

from .forms import (
    OwnerForm,
    DogForm,
    ReservationForm,
    TestimonialForm,
    CommentForm
)

# RESERVATIONS VIEWS:

# Reservations Create View


@login_required
def reservations(request):
    owner_form = OwnerForm()
    dog_form = DogForm()
    reservation_form = ReservationForm()

    if request.method == 'POST':
        owner_form = OwnerForm(request.POST)
        dog_form = DogForm(request.POST)
        reservation_form = ReservationForm(request.POST)

        if (
            owner_form.is_valid() and
            dog_form.is_valid() and
            reservation_form.is_valid()
        ):
            owner, created = Owner.objects.get_or_create(user=request.user)
            owner.name = owner_form.cleaned_data.get('name')
            owner.tel_no = owner_form.cleaned_data.get('tel_no')
            owner.email_address = owner_form.cleaned_data.get('email_address',)
            owner.save()

            cleaned_data = dog_form.cleaned_data

            dog = Dog.objects.create(
                owner=owner,
                name=dog_form.cleaned_data['name'],
                gender=dog_form.cleaned_data['gender'],
                breed=dog_form.cleaned_data['breed'],
                food_provided=dog_form.cleaned_data['food_provided'],
                vaccinations_up_to_date=cleaned_data['vaccinations_up_to_date']
            )

            reservation = reservation_form.save(commit=False)
            reservation.owner = owner
            reservation.dog = dog
            reservation.save()

            messages.success(request, 'Reservation successfully created!')

        else: 
            messages.error(request, 'Please correct the errors below.')

        
    existing_reservations = Reservation.objects.filter(
        owner__user=request.user
        )

    context = {
        'owner_form': owner_form,
        'dog_form': dog_form,
        'reservation_form': reservation_form,
        'existing_reservations': existing_reservations,
    }
    return render(
        request,
        'islandersdogdaycare/reservations.html', context)

# Reservations Read View

@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(owner__user=request.user)
    return render(request, 'islandersdogdaycare/reservation_list.html', {'reservations': reservations})

@login_required
def reservation_detail(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id, owner__user=request.user)
    return render(request, 'islandersdogdaycare/reservation_detail.html', {'reservation': reservation})

# Reservations Update View

@login_required
def update_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    owner = reservation.dog.owner
    dog = reservation.dog

    if request.method == "POST":
        reservation_form = ReservationForm(request.POST, instance=reservation)
        owner_form = OwnerForm(request.POST, instance=owner)
        dog_form = DogForm(request.POST, instance=dog)

        if reservation_form.is_valid()and owner_form.is_valid() and dog_form.is_valid():
            owner_form.save()
            dog_form.save()
            reservation_form.save()
            messages.success(request, 'Reservation updated successfully!')
            return redirect(reverse('reservation_detail', args=[reservation.id]))

    else:
        reservation_form = ReservationForm(instance=reservation)
        owner_form = OwnerForm(instance=owner)
        dog_form = DogForm(instance=dog)

    context = {
        'reservation_form': reservation_form,
        'owner_form': owner_form,
        'dog_form': dog_form,
    }

    return render(request, 'islandersdogdaycare/update_reservation.html', context)

# Reservations Delete View

@login_required
def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id, owner__user=request.user)
    if request.method == "POST":
        reservation.delete()
        messages.success(request, 'Reservation deleted successfully!')
        return redirect('reservation_list')
    return render(request, 'islandersdogdaycare/delete_reservation.html', {'reservation': reservation})



# Testimonials and comments View


def testimonials(request):
    comment_form = CommentForm()
    testimonial_form = TestimonialForm()
    all_testimonials = (
        Testimonial.objects
        .filter(status=1, approved=True)
        .order_by('-created_on')
    )

    if request.method == 'POST':

        if 'submit_comment' in request.POST:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                testimonial_id = request.POST.get('testimonial_id')
                new_comment.testimonial = get_object_or_404(
                    Testimonial, id=testimonial_id)
                new_comment.user = request.user
                new_comment.save()
                return redirect('testimonials')

        elif 'submit_testimonial' in request.POST:
            testimonial_form = TestimonialForm(request.POST, request.FILES)
            if testimonial_form.is_valid():
                new_testimonial = testimonial_form.save(commit=False)
                new_testimonial.author = request.user
                new_testimonial.save()
                messages.success(
                    request, 'Your testimonial is awaiting approval.')
                return redirect('testimonials')

    else:
        comment_form = CommentForm()
        testimonial_form = TestimonialForm()

    return render(request, 'islandersdogdaycare/testimonials.html', {
        'testimonials': all_testimonials,
        'comment_form': comment_form,
        'testimonial_form': testimonial_form
    })

# Login View


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})

# Logout View


def logout(request):
    auth_logout(request)
    return redirect('index')


# Home page View


def index(request):
    return render(request, 'islandersdogdaycare/index.html')

# custom Error Views


def custom_page_not_found_view(request, exception):
    return render(request, 'islandersdogdaycare/404.html', {})


def custom_permission_denied_view(request, exception):
    return render(request, 'islandersdogdaycare/403.html', {})
