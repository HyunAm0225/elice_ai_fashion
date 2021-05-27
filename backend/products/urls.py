from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'product'
router = routers.DefaultRouter()
# router.register(r'product', views.ProductViewSet)
router.register(r'likeproduct', views.LikeProductViewSet)


urlpatterns = [
    path('fashion/', views.ProductViewset.as_view({'get': 'list'}), name='fashion'),
    path('likeproduct/', views.LikeProductView.as_view(), name='likeproduct'),
    path('', include(router.urls)),
]
