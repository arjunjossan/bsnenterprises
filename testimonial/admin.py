from django.contrib import admin

# Register your models here.
from django.contrib import admin
from testimonial.models import Testimonial

# Register your models here.

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('testimonial_img','testimonial_name','testimonial_position','testimonial_rating','testimonial_desc')

admin.site.register(Testimonial,TestimonialAdmin)