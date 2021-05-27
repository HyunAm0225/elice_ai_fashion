from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields ='__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeProduct
        fields ='__all__'