from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response

import json


User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all(), message="이미 존재하는 아이디 입니다.")])
    password = serializers.CharField(
        write_only=True, style={'input_type': 'password', 'placeholder': 'Password'}, validators=[validate_password])
    full_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
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
        fields = ('username', 'password', 'full_name', 'email', 'token')
