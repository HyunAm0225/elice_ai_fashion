from django.urls import path
from .views import productView, LikeProductView
from rest_framework import routers

app_name = 'product'

urlpatterns = [
    path('fashion/', productView.as_view(), name='fashion'),
    path('likeproduct/', LikeProductView.as_view(), name='likeproduct'),
]
