from rest_framework import generics
from api.serializers import StatusSerializer
from core.models import Status

class StatusListView(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
