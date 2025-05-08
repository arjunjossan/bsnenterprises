from django.contrib import admin
from indexpurifier.models import indexPurifier


# Register your models here.

class indexPurifierAdmin(admin.ModelAdmin):
    list_display = ('ip_off','ip_img','ip_stock','ip_title','ip_rating','ip_price','ip_strikeprice','ip_save','ip_sp1','ip_sp2','ip_sp3')

admin.site.register(indexPurifier,indexPurifierAdmin)