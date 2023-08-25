from django.db import models
from django.contrib.auth.models import User


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
        related_name='dog',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        null=True,
        blank=True)
    breed = models.CharField(max_length=50)
    food_provided = models.CharField(
        max_length=3,
        choices=FOOD_PROVIDED_CHOICES,
        null=True,
        blank=True)
    vaccinations_up_to_date = models.CharField(
        max_length=3,
        null=True,
        blank=True,
        choices=VACCINATION_CHOICES)

    def __str__(self):
        return self.name


# Reservation Model
class Reservation(models.Model):
    owner = models.ForeignKey(
        Owner,
        related_name='reservation',
        on_delete=models.CASCADE)
    dog = models.ForeignKey(
        Dog,
        related_name='reservation',
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

class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    approved = models.BooleanField(default=False, null=True)

    def __str__(self):
        return F"Testimonial by {self.user.username}"


# Comment Model

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    testimonial = models.ForeignKey(
        Testimonial, related_name='comment',
        on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return F"Comment by {self.user.username}"
