from rest_framework import serializers

class pedidoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('__all__')