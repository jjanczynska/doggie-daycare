from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Owner, Dog, Reservation, ExtraInfo, Testimonial, Comment
from .models import Post
