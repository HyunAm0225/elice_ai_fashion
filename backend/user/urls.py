from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from rest_framework import routers
from django.conf.urls import include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

app_name = 'user'
router = routers.DefaultRouter()
router.register(r'closet', views.ClosetViewSet)
# router.register('user', views.UserCreateSerializer)

urlpatterns = [
    # 장고 앱
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('current/', views.CurrentView.as_view(), name='current'),
    path('login/', obtain_jwt_token, name='login'),

    path('', include(router.urls)),
    # path('logout/', refresh_jwt_token),
]
