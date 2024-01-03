from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reservations/', views.reservations, name='reservations'),
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservations/<int:reservation_id>/', views.reservation_detail, name='reservation_detail'),
    path('reservations/update/<int:reservation_id>/', views.update_reservation, name='update_reservation'),
    path('reservations/delete/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
