from django.contrib import admin
from .models import Owner, Dog, Reservation, Testimonial, Comment


# Models registeration
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['user', 'tel_no']


admin.site.register(Owner, OwnerAdmin)
admin.site.register(Dog)
admin.site.register(Reservation)
admin.site.register(Testimonial)
admin.site.register(Comment)

