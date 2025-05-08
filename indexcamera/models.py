
# Create your models here.
from django.db import models


# Create your models here.

class indexCamera(models.Model):
    ic_img = models.CharField(max_length=400)
    # ic_stock = models.CharField(max_length=50)
    # ic_rating = models.CharField(max_length=200)
    ic_strikeprice = models.CharField(max_length=200)
    ic_price = models.CharField(max_length=200)
    ic_title = models.CharField(max_length=200)
    ic_sp1 = models.CharField(max_length=200)
    ic_sp2 = models.CharField(max_length=200)
    ic_sp3 = models.CharField(max_length=200)
    