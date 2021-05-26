from django.shortcuts import render
from .models import User, Closet
from .serializers import UserCreateSerializer, ClosetSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework_jwt.views import RefreshJSONWebToken
from rest_framework.views import APIView
from rest_framework import status, viewsets
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.http import HttpResponse


# Create your views here.


class SignupView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer
    permission_classes = [
        AllowAny
    ]

    def post(self, request, formet=None):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CurrentView(APIView):
    def get(self, request):
        data = User.objects.filter(email=request.user)
        user_data = serializers.serialize('json', data)
        return HttpResponse(user_data, content_type="text/json-comment-filtered; charset=utf-8")


class ClosetViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     AllowAny
    # ]
    permission_classes = (IsAuthenticated,)
    serializer_class = ClosetSerializer
    queryset = Closet.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(user_id=self.request.user.id)   # added string
