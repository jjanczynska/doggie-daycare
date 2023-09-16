from django.contrib import admin
from .models import Owner, Dog, Reservation, Testimonial, Comment

# SAdmin actions for approving testimonials


def approve_testimonials(modeladmin, request, queryset):
    queryset.update(approved=True)
    approve_testimonials.short_description = "Approve selected testimonials"


# Models registeration
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['user', 'tel_no']


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'sreated_on', 'approved']
    ordering = [approve_testimonials]


admin.site.register(Owner, OwnerAdmin)
admin.site.register(Dog)
admin.site.register(Reservation)
admin.site.register(Testimonial)
admin.site.register(Comment)
