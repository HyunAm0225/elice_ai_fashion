from django.contrib import admin
from .models import Product, LikeProduct
from django.utils.html import format_html


class LikeInline(admin.TabularInline):
    model = Product.likeproduct.through
    verbose_name = "like"


class ProductAdmin(admin.ModelAdmin):
    def product_cover_thumbnail(self, obj):
        return format_html('<img src="{}" width="50px;"/>'.format(obj.thumnail))
    product_cover_thumbnail.short_description = "Thumbnail"
    list_display = ('id', 'name', 'brand', 'product_cover_thumbnail', 'category', 'color', 'discount_rate')

    search_fields = ['name']
    inlines = (LikeInline,)

    def __str__(self):
        return self.name


class LikeProductAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'product_id', 'is_like')


admin.site.register(Product, ProductAdmin)
admin.site.register(LikeProduct, LikeProductAdmin)
