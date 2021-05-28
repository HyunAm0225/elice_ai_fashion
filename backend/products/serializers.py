from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['-id']
        model = Product
        fields ='__all__'
        extra_kwargs = {'likeproduct': {'required': False}}

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeProduct
        fields ='__all__'