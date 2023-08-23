from django.contrib import admin
from .models import Owner, Dog, Reservation, ExtraInfo


# Models registeration
admin.site.register(Owner)
admin.site.register(Dog)
admin.site.register(Reservation)
admin.site.register(ExtraInfo)
