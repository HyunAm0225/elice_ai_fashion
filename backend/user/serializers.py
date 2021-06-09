from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from .models import Closet
from user.temp import get_feature as get_fe
from user.temp import yolo_init
from django.conf import settings


import json


User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all(), message="이미 존재하는 아이디 입니다.")])
    password = serializers.CharField(
        write_only=True, style={'input_type': 'password', 'placeholder': 'Password'}, validators=[validate_password])
    username = serializers.CharField(required=True)
    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('email', 'password', 'username', 'token')


class ClosetSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(use_url=True)
    feature = serializers.SerializerMethodField()

    def get_feature(self, style):
        yolo_net, YOLO_LABELS = yolo_init()
        image = f"{settings.BASE_DIR}{style.dress_img.url}"
        feature = get_fe(yolo_net, image, YOLO_LABELS)
        # print(feature)
        return feature

    def create(self, validated_data):
        closet = Closet.objects.create(**validated_data)
        closet.feature = self.get_feature(closet)
        # print(closet)
        closet.save()
        return closet

    class Meta:
        model = Closet
        fields = '__all__'
