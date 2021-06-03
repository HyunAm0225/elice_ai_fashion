import random
import json
from .models import Product, LikeProduct
from user.models import User
from .serializers import ProductSerializer, LikeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers, status, generics
from django_filters import rest_framework as filters
from django.http import HttpResponse, JsonResponse
from .pagination import CustomResultsSetPagination

class ProductView(generics.ListAPIView):
    model = Product
    queryset = Product.objects.get_queryset().order_by('?')
    serializer_class = ProductSerializer
    permission_classes = [
        AllowAny
    ]
    pagination_class = CustomResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,) 
    filter_fields = ('category',)


class RecommendView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        IsAuthenticated
    ]
    pagination_class = CustomResultsSetPagination


class LikeProductView(APIView):
    model = LikeProduct
    serializer_class = LikeSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)
        print(user_data, request.user.pk)
        if not LikeProduct.objects.filter(product_id=user_data['id'], user_id=request.user.pk).exists():
            LikeProduct.objects.create(
                user_id=request.user,
                product_id=Product.objects.get(id=user_data['id']),
                is_like=True
            ).save
            return HttpResponse('good', status=200)

        delete_product = LikeProduct.objects.get(product_id=user_data['id'], user_id=request.user.pk)
        delete_product.delete()

        return HttpResponse({'message': 'DELETE_LIKE_PRODUCT'}, status=200)

    def get(self, request, *args, **kwargs):
        like_list = []
        like_products = LikeProduct.objects.filter(user_id=request.user.pk).values_list()
        for like_product in like_products:
            products = Product.objects.filter(id=str(like_product[2]))
            is_like_list = LikeProduct.objects.filter(product_id=str(like_product[2])).values_list()
            is_like = (list(is_like_list)[0][3])
            product_list = list(products.values())
            product_list[0]['likeproduct'] = is_like
            like_list.append(product_list[0])

        return JsonResponse({'like_list': like_list})
