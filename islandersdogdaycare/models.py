from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField


# Owner Model
class Owner(models.Model):
    user = models.OneToOneField(
        User,
        related_name='owner_profile',
        on_delete=models.CASCADE)
    tel_no = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username


# Dog Model
class Dog(models.Model):

    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    VACCINATION_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    FOOD_PROVIDED_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    owner = models.ForeignKey(
        Owner,
        related_name='dogs',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
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
        related_name='reservations',
        on_delete=models.CASCADE)
    dog = models.ForeignKey(
        Dog,
        related_name='reservations',
        on_delete=models.CASCADE)
    date_of_daycare = models.DateField()

    def __str__(self):
        return (
            f"{self.owner.user.username}'s reservation for "
            f"{self.dog.name} on {self.date_of_daycare}"
        )


# ExtraInfo Model
class ExtraInfo(models.Model):
    reservation = models.OneToOneField(
        Reservation,
        related_name='extra_info',
        on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Extra information for {self.reservation}"


# Testimonial Model

STATUS = ((0, "Draft"), (1, "Published"))


class Testimonial(models.Model):
    title = models.CharField(
        max_length=500, unique=True,
        default='Testimonial Title')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="testimonials",
        null=True, default=None
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
        return f"Testimonial by {self.author.username}"


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
        return F"Comment by {self.user.username}"
