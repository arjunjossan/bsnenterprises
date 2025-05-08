from django.contrib import admin
from blogs.models import Blogs

# Register your models here.

class BlogsAdmin(admin.ModelAdmin):
    list_display = ('blogs_img','blogs_title','blogs_area','blogs_desc','blogs_name','blogs_date')

admin.site.register(Blogs,BlogsAdmin)