from django.urls import path, include
from rest_framework import routers
from style import views
app_name = 'style'
router = routers.DefaultRouter()
router.register(r'style', views.StyleViewset)
urlpatterns = [
    path('', include(router.urls)),
]
