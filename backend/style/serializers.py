from style.models import Style
from user.models import User
from rest_framework import serializers


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(read_only=True)

    class Meta:
        model = User
        fields = ['email', 'styles']
        read_only_fields = ['email']
