from django.contrib import admin
from .models import Product


class CrawlAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'brand', 'category', 'discount_rate')

admin.site.register(Product, CrawlAdmin)