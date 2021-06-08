from django.urls import path, include
from rest_framework import routers
from style import views
app_name = 'style'
router = routers.DefaultRouter()
router.register(r'stylelist', views.StyleViewset, basename='stylelist')
router.register(r'style', views.SelectViewset, basename='style')
urlpatterns = [
    path('', include(router.urls)),
    # path('style/', views.SelectViewset)
]
