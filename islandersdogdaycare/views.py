from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Owner, Dog, Reservation, ExtraInfo, Testimonial, Comment
from .forms import ReservationForm, TestimonialForm, CommentForm

# Reservations View:


@login_required
def reservations(request):
    if request.method == 'POST':
        action = request.POST.get('action') 
        
        if action == 'create':
            form = ReservationForm(request.POST)
            if form.is_valid():
                reservation = form.save(commit=False)
                reservation.owner = get_object_or_404(Owner, user=request.user)
                reservation.save()
                return redirect('reservations')
        
        elif action == "edit":
            reservation_id = request.POST.get('reservation_id')
            reservation = get_object_or_404(Reservation, id=reservation_id)
            form = ReservationForm(request.POST, instance=reservation)
            if form.is_valid():
                form.save()
                return redirect('reservations')
        
        elif action == "delete":
            reservation_id = request.POST.get('reservation_id')
            reservation = get_object_or_404(Reservation, id=reservation_id)
            reservation.delete()
            return redirect('reservations')
            
    reservations = Reservation.objects.filter(owner__user=request.user)
    form = ReservationForm()
    return render(
        request, 'reservations.html', {
            'reservations': reservations, 'form': form}
    )
