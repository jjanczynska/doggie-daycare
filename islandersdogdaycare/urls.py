from django.urls import path
from views import reservations, testimonials

urlpatters = [
    path('reservations/', views.reservations, name='reservations'),
    path(
        'testimonials/<int:testimonial_id>/',
        views.testimonials, name='testimonials'),

]