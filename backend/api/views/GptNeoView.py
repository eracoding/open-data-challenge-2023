from rest_framework import generics
from api.serializers import GptNeoSerializer
from core.models import GptNeo


class GptNeoListView(generics.ListAPIView):
    queryset = GptNeo.objects.all()
    serializer_class = GptNeoSerializer
