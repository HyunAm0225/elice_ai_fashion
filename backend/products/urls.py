from django.urls import path
from . import views

app_name = 'product'


urlpatterns = [
    path('fashion/', views.ProductListView.as_view(), name='fashion'),
    path('likeproduct/', views.LikeProductView.as_view()),
]
