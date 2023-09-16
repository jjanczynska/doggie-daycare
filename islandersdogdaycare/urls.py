from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reservations/', views.reservations, name='reservations'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
