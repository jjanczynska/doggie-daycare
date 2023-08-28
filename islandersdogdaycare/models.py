from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField


# Owner Model
class Owner(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        primary_key=True)
    name = models.CharField(max_length=100, default="Default Name")
    tel_no = models.CharField(max_length=15)
    email_address = models.EmailField(default="default@example.com")

    def __str__(self):
        return self.user.username


# Dog Model
class Dog(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    owner = models.ForeignKey(
        Owner,
        related_name='dogs',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        null=True,
        blank=True)
    breed = models.CharField(max_length=50)
    food_provided = models.BooleanField(default=False)
    vaccinations_up_to_date = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# Reservation Model
class Reservation(models.Model):
    owner = models.ForeignKey(
        Owner, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    date_of_daycare = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Reservation for {self.dog.name} on {self.date_of_daycare}"


# Testimonial Model

STATUS = ((0, "Draft"), (1, "Published"))


class Testimonial(models.Model):
    title = models.CharField(
        max_length=500, unique=True,
        default='Testimonial Title')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Testimonials',
        default='User'
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        if self.author:
            return f"Testimonial by {self.author.username}"
        else:
            return "Anonymous Testimonial"


# Comment Model

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    testimonial = models.ForeignKey(
        Testimonial, related_name='comments', on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.user.username}"
