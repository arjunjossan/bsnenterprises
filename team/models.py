from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Team(models.Model):
    team_pic = models.CharField(max_length=200)
    team_name = models.CharField(max_length=20)
    team_field = models.CharField(max_length=20)
    # team_desc = models.TextField()
    team_desc = HTMLField()
    