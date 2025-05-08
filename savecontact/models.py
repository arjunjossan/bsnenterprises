from django.db import models

# Create your models here.

class saveContact(models.Model):
    s_name = models.CharField(max_length=200)
    s_contact = models.CharField(max_length=20, blank=True, null=True)
    s_email = models.CharField(max_length=20)
    s_message = models.CharField(max_length=20)

    