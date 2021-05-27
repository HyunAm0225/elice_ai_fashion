import random, json
from .models import Product, LikeProduct
from user.models import User
from .serializers import ProductSerializer, LikeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers, status
from django.http import HttpResponse, JsonResponse

class productView(APIView):
    model = Product
    serializer_class = ProductSerializer
    permission_classes = [
        AllowAny
    ]

    def get(self):
        products = Product.objects.all() 
        product_list = list(products)
        random.shuffle(product_list)
        serializer = ProductSerializer(product_list, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)


class LikeProductView(APIView):
    model = LikeProduct
    serializer_class = LikeSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = [
        IsAuthenticated
    ]
    
    def post(self, request):
        user_data = json.loads(request.body)
        print(user_data, request.user.pk)
        if not LikeProduct.objects.filter(product_id = user_data['id'], user_id = request.user.pk).exists():
            LikeProduct.objects.create(
                user_id=request.user,
                product_id=Product.objects.get(id = user_data['id'])
            ).save
            return HttpResponse('good', status=200)

        delete_product = LikeProduct.objects.get(product_id = user_data['id'], user_id = request.user.pk)
        delete_product.delete()

        return HttpResponse({'message': 'DELETE_LIKE_PRODUCT'}, status=200)


    def get(self, request):
        like_list = [] 
        like_products = LikeProduct.objects.filter(user_id = request.user.pk).values_list()
        for like_product in like_products:
            products = Product.objects.filter(id = str(like_product[2])) 
            product_list = list(products.values())
            like_list.append((product_list))
        return JsonResponse({'like_list':like_list})
