from django.db import models

# Create your models here.
from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Slider(models.Model):
    slider_img = models.CharField(max_length=200)
    slider_title = models.CharField(max_length=200)
    slider_desc = HTMLField()
    