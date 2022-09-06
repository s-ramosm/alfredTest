from dataclasses import field
from rest_framework import serializers

class conductorSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('__all__')