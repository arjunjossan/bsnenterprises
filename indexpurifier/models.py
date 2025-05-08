
# Create your models here.
from django.db import models


# Create your models here.

class indexPurifier(models.Model):
    ip_off = models.CharField(max_length=20)
    ip_img = models.CharField(max_length=400)
    ip_stock = models.CharField(max_length=50)
    ip_title = models.CharField(max_length=200)
    ip_rating = models.CharField(max_length=200)
    ip_price = models.CharField(max_length=200)
    ip_strikeprice = models.CharField(max_length=200)
    ip_save = models.CharField(max_length=200)
    ip_sp1 = models.CharField(max_length=200)
    ip_sp2 = models.CharField(max_length=200)
    ip_sp3 = models.CharField(max_length=200)
    