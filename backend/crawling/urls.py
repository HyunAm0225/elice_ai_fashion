from django.urls import path
from . import views

app_name = 'crawling'


urlpatterns = [
    path('fashion/', views.ProductListView.as_view(), name='fashion')
]
