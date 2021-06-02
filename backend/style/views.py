from django.shortcuts import render
from style.models import Style
from style.serializers import StyleSerializer
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny

# Create your views here.


class StyleViewset(viewsets.ModelViewSet):
    permission_classes = [
        AllowAny
    ]
    serializer_class = StyleSerializer
    queryset = Style.objects.all()

    # def get_queryset(self):
    #     return super().get_queryset().filter(user_id=self.request.user.id)   # added string
