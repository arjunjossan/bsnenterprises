from django.db import models

# Create your models here.
from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Blogs(models.Model):
    blogs_img = models.CharField(max_length=200)
    blogs_title = models.CharField(max_length=200)
    blogs_area = models.CharField(max_length=200)
    blogs_desc = HTMLField()
    blogs_name = models.CharField(max_length=200)
    blogs_date = models.CharField(max_length=200)
    