import random
import json
from .models import Product, LikeProduct
from style.models import Style
from .serializers import ProductSerializer, LikeSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import  generics
from django_filters import rest_framework as filters
from django.http import HttpResponse, JsonResponse
from .pagination import CustomResultsSetPagination

class ProductView(generics.ListAPIView):
    """
    url주소에서 category와 page_size를 받아 상품을 출력해주는 api
    :param url: 불러올 url
    :return:
    """
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
        AllowAny
    ]
    pagination_class = CustomResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend,) 
    filter_fields = ('category',)

    def get(self, request):
        recommend_list = []
        request = (json.loads(request.body))
        for i in request['styles']:
            style = list(Style.objects.filter(id=i).values_list())[0][2]
            for category, color in style.items():
                recommend_list.append(list(Product.objects.filter(category=category,color=color).values()))
        
        return JsonResponse({'recommend_list': recommend_list})




class LikeProductView(generics.ListAPIView):
    model = LikeProduct
    serializer_class = LikeSerializer
    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request, format=None):
        if not LikeProduct.objects.filter(product_id=request.data['product_id'], user_id=request.user.pk).exists():
            LikeProduct.objects.create(
                user_id=request.user,
                product_id=Product.objects.get(id=request.data['product_id']),
                is_like=True
            ).save
            return HttpResponse({'message': 'CREATE_LIKE_PRODUCT'}, status=200)

        delete_product = LikeProduct.objects.get(product_id=request.data['product_id'], user_id=request.user.pk)
        delete_product.delete()
        return HttpResponse({'message': 'DELETE_LIKE_PRODUCT'}, status=200)


    def get(self, request, format=None):
        queryset =LikeProduct.objects.filter(user_id=request.user.pk)
        serializer = LikeSerializer(queryset, many=True)
        return Response(serializer.data)
