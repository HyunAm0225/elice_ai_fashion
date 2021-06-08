from django.shortcuts import render
from style.models import Style
from user.models import User
from style.serializers import StyleSerializer, ChoiceSerializer
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# Create your views here.


class StyleViewset(viewsets.ViewSet):
    permission_classes = [
        AllowAny,
    ]

    def list(self, request):
        queryset = Style.objects.all()
        serializer_class = StyleSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        queryset = Style.objects.all()
        style = get_object_or_404(queryset, pk=pk)
        serializer = StyleSerializer(style)
        return Response(serializer.data)


class SelectViewset(viewsets.ModelViewSet):
    permission_classes = [
        AllowAny
    ]
    serializer_class = ChoiceSerializer
    queryset = User.objects.all()
