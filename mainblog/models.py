
from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class MainBlog(models.Model):
    main_blog_img = models.CharField(max_length=200)
    main_blog_news = models.CharField(max_length=200)
    main_blog_title = models.CharField(max_length=200)
    main_blog_desc = HTMLField()
    