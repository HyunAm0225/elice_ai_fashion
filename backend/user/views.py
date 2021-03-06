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
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        print(request.user)
        email = request.user.email
        username = request.user.username
        pk = request.user.pk
        styles = request.user.styles.all().values()
        user_data = {"pk": pk, "username": username, "email": email, "styles": styles}
        return Response(user_data, status=status.HTTP_200_OK)


class ClosetViewSet(viewsets.ModelViewSet):
    # permission_classes = [
    #     AllowAny
    # ]
    permission_classes = (IsAuthenticated,)
    serializer_class = ClosetSerializer
    queryset = Closet.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(user_id=self.request.user.id)   # added string
