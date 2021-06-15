from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['-id']
        model = Product
        fields ='__all__'
        extra_kwargs = {'likeproduct': {'required': False}}

class LikeSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer(read_only = True)
    class Meta:
        model = LikeProduct
        fields =['id', 'is_like', 'user_id', 'product_id']