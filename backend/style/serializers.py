from style.models import Style
from rest_framework import serializers


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = '__all__'
