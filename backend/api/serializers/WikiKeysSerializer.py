from rest_framework import serializers
from core.models import WikiKeys


class WikiKeysSerializer(serializers.ModelSerializer):
    class Meta:
        model = WikiKeys
        fields = "__all__"
