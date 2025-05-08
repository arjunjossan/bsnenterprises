from django.contrib import admin
from mainblog.models import MainBlog

# Register your models here.

class MainBlogAdmin(admin.ModelAdmin):
    list_display = ('main_blog_img','main_blog_news','main_blog_title','main_blog_desc')

admin.site.register(MainBlog,MainBlogAdmin)