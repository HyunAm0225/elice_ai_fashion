from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name="상품 이름")
    brand = models.CharField(max_length=30, verbose_name="브랜드") 
    sale_price = models.FloatField(verbose_name="판매가")
    price = models.FloatField(verbose_name="원가")
    discount_rate = models.IntegerField(verbose_name="할인율")
    url = models.URLField(max_length=2000, verbose_name="상품 url")
    thumnail = models.URLField(max_length=2000, verbose_name="대표 이미지")
    category = models.CharField(max_length=200, default="clothes", verbose_name="카테고리")
    color = models.CharField(max_length=20, verbose_name="색상")
    star = models.BooleanField(default="false", verbose_name="찜 유무")
    
    class Meta:
        db_table = 'Product'
        verbose_name = "상품"

    def __str__(self):
        return self.name