from dataclasses import field
from rest_framework import serializers
from .models import conductor

class conductorSerializer(serializers.ModelSerializer):

    class Meta:
        model  = conductor
        fields = '__all__'