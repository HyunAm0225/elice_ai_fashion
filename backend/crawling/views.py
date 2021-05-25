from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import random
from .models import Product, LikeProduct
import json
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# Create your views here.
class ProductListView(View):
    def get(self):
        # _category = catregory_name
        products = Product.objects.all()
        # products = Product.objects.filter(category = _category)
        products_list = []

        for product in products:
            products_list.append({
                'name' : product.name,
                'brand' : product.brand,
                'sale_price' : product.sale_price,
                'price' : product.price,
                'discount_rate' : product.discount_rate,
                'thumnail' : product.thumnail,
                'url' : product.url,
                'category' : product.category,
                'color' : product.color,
                'star' : product.star,
            })
        
        random.shuffle(products_list)
        return JsonResponse({'product_list': products_list}, status = 200)

class LikeProductView(View):
    @api_view(['POST'])
    @permission_classes((IsAuthenticated, ))
    @authentication_classes((JSONWebTokenAuthentication,))
    def post(self, request):
        user_data = json.loads(request.body)

        if not LikeProduct.objects.filter(product_id = user_data['product_id'], user_id = request.user.id).exists():
            LikeProduct.objects.create(
                user    = request.user,
                product = Product.objects.get(id = user_data['product_id'])
            ).save

            return JsonResponse({'message':'ADD_LIKE_PRODUCT'}, status=200)

        delete_product = LikeProduct.objects.get(product_id = user_data['product_id'], user_id = request.user.id)
        delete_product.delete()

        return JsonResponse({'message':'DELETE_LIKE_PRODUCT'}, status=200)

    @api_view(['GET'])
    @permission_classes((IsAuthenticated, ))
    @authentication_classes((JSONWebTokenAuthentication,))
    def get(self, request):
        like_list    = []
        like_product = LikeProduct.objects.filter(user_id = request.user.id).prefetch_related("product")
        
        for product in like_product:
            data = {
                "id"           : product.product.id,
                "product_line" : product.product.product_line,
                "name"         : product.product.name,
                "price"        : product.product.price,
                "sale_price"   : product.product.sale_price,
                "hash_tag"     : product.product.hash_tag,
                "images"       : product.product.image_set.first().image_url,
                "sale"         : product.product.productflag_set.first().sale_flag,
                "gift"         : product.product.productflag_set.first().gift_flag
            }

            like_list.append(data)

        return JsonResponse({'like_list' : like_list})