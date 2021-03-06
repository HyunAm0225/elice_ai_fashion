from django.urls import path
from .views import ProductView, LikeProductView, RecommendView

app_name = 'product'

urlpatterns = [
    path('fashion/', ProductView.as_view(), name='fashion'),
    path('likeproduct/', LikeProductView.as_view(), name='likeproduct'),
    path('recommend/', RecommendView.as_view(), name='likeproduct'),
]
