from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from categorias.models import *
from .serializers import *
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend 

class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    #queryset = Category.objects.filter(published=True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['published','title']
