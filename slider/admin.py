from django.contrib import admin
from slider.models import Slider

# Register your models here.

class SliderAdmin(admin.ModelAdmin):
    list_display = ('slider_img','slider_title','slider_desc')

admin.site.register(Slider,SliderAdmin)