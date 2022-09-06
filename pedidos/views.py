from django import views
from django.shortcuts import render
from rest_framework.viewsets import ViewSet
#Model
from .models import pedido
#Serializer
from .serializers import pedidoSerializer

class pedidoViewSet(ViewSet):

    serializer_class = pedidoSerializer
    queryset = pedido.objects.all()
