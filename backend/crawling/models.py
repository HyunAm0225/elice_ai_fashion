from django.db import models

# Create your models here.

class Crawl_data(models.Model):
    name = models.CharField(max_length=100) 
    brand = models.CharField(max_length=200) 
    sale_price = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    discount_rate = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)