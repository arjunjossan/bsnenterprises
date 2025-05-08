# Create your models here.
from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Testimonial(models.Model):
    testimonial_img = models.CharField(max_length=200)
    testimonial_name = models.CharField(max_length=200)
    testimonial_position = models.CharField(max_length=200)
    testimonial_rating = models.CharField(max_length=200)
    testimonial_desc = HTMLField()
    