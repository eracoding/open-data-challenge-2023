import rest_framework.views
from rest_framework import generics
from rest_framework.response import Response

from api.serializers import CategorySerializer
from core.models import Category


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CategoryCreateView(generics.CreateAPIView, generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DeleteCategory(rest_framework.views.APIView):
    def delete(self, request):
        Category.objects.all().delete()
        return Response()
