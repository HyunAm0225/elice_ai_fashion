from django.urls import path
from . import views
from rest_framework import routers
from django.conf.urls import include


router = routers.DefaultRouter()
app_name = 'user'
# router.register('user', views.UserCreateSerializer)

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
]
