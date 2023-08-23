from django.db import models
from django.contrib.auth.models import User


# Owner Model
class Owner(models.Model):
    User = models.OneToOneField(
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
        related_name='dogs',
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
            f"{self.dog_name} on {self.date_of_daycare}"
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
