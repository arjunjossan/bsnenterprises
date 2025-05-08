from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Banner(models.Model):
    banner_text =  models.CharField(max_length=200)
    banner_detail = HTMLField()
    