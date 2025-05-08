
from django.contrib import admin
from savecontact.models import saveContact

# Register your models here.

class saveContactAdmin(admin.ModelAdmin):
    list_display = ('s_name','s_contact','s_email','s_message')

admin.site.register(saveContact,saveContactAdmin)