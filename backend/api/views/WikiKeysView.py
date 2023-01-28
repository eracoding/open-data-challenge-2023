from rest_framework import generics
from api.serializers import WikiKeysSerializer
from core.models import WikiKeys


class WikiKeysListView(generics.ListAPIView):
    queryset = WikiKeys.objects.all()
    serializer_class = WikiKeysSerializer
