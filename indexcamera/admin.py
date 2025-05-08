from django.contrib import admin
from indexcamera.models import indexCamera


# Register your models here.

class indexCameraAdmin(admin.ModelAdmin):
    list_display = ('ic_img','ic_strikeprice','ic_price','ic_title','ic_sp1','ic_sp2','ic_sp3')

admin.site.register(indexCamera,indexCameraAdmin)