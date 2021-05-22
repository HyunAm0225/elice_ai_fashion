from django.urls import path
from . import views

urlpatterns = [
    path('category/<str:catregory_name>', views.ProductListView.as_view())
]