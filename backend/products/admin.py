from django.contrib import admin
from .models import Product, LikeProduct


class LikeInline(admin.TabularInline):
    model = Product.likeproduct.through
    verbose_name = "like"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'category', 'discount_rate')
    search_fields = ['name']
    inlines = (LikeInline,)

    def __str__(self):
        return self.name


class LikeProductAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'product_id', 'is_like')


admin.site.register(Product, ProductAdmin)
admin.site.register(LikeProduct, LikeProductAdmin)
