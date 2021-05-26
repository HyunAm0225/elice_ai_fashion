from django.contrib import admin
from .models import Product, LikeProduct


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'brand', 'category', 'discount_rate')

admin.site.register(Product, ProductAdmin)
admin.site.register(LikeProduct)