from django.contrib import admin
from team.models import Team

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_pic','team_name','team_field','team_desc')

admin.site.register(Team,TeamAdmin)