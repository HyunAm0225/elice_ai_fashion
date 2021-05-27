from django.db import models
from django.conf import settings
from user.models import User

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="상품 이름")
    brand = models.CharField(max_length=100, verbose_name="브랜드") 
    sale_price = models.FloatField(verbose_name="판매가")
    price = models.FloatField(verbose_name="원가")
    discount_rate = models.IntegerField(verbose_name="할인율")
    url = models.URLField(max_length=2000, verbose_name="상품 url")
    thumnail = models.URLField(max_length=2000, verbose_name="대표 이미지")
    category = models.CharField(max_length=200, default="clothes", verbose_name="카테고리")
    color = models.CharField(max_length=20, verbose_name="색상")
    likeproduct = models.ManyToManyField(User, through = 'LikeProduct', related_name = 'like_product', blank=True)
    
    class Meta:
        db_table = 'Product'
        verbose_name = "상품"

    def __str__(self):
        return self.name

class LikeProduct(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='like_product', blank=True,db_column='product_id')

    class Meta:
        db_table = "likeproducts"