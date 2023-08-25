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
    owner = models.ForeignKey(
        Owner,
        related_name='dog',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    bring_own_food = models.BooleanField()
    up_to_date_vaccinations = models.BooleanField()

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
