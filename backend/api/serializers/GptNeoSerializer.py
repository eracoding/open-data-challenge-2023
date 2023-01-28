from rest_framework import serializers
from core.models import GptNeo


class GptNeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GptNeo
        fields = "__all__"
