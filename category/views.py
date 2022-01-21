from category.models import Category
from category.serializers import CategorySerializer
from rest_framework import routers, serializers, viewsets, permissions


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(level=0)
    serializer_class = CategorySerializer
    http_method_names = ['get']
    permission_classes = [permissions.AllowAny]