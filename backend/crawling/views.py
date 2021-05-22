from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from .models import Product
# Create your views here.
class ProductListView(View):
    def get(self, request, catregory_name):
        _category = catregory_name
        print(_category)
        products = Product.objects.all()
        products = Product.objects.filter(category = _category)
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
        return JsonResponse({f'{_category}_product_list': products_list}, status = 200)
        #JsonResponse({f'{_category}_product_list': products_list}, status = 200)

        