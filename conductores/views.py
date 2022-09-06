from django.shortcuts import render
from rest_framework.viewsets import ViewSet
#Model 
from .models import conductor
#Serializer
from .serializers import conductorSerializer



class conductoresViewSet(ViewSet):
    serializer_class = conductorSerializer
    queryset = conductor.objects.all()


