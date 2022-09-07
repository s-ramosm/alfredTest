from django import views
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
#Model
from .models import pedido
#Serializer
from .serializers import pedidoSerializer

class pedidoViewSet(ModelViewSet):

    serializer_class = pedidoSerializer
    queryset = pedido.objects.all()
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    ordering_fields = ['hora']
    filterset_fields = ['conductor','fecha']
