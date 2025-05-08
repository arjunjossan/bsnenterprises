from django.contrib import admin
from banner.models import Banner

# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display = ('banner_text','banner_detail')

admin.site.register(Banner,BannerAdmin)