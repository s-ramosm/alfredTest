from rest_framework import serializers
from .models import pedido
import datetime

class pedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = pedido
        fields = '__all__'

    def validate(self, data):

        horafinal = datetime.time(
            data["hora"].hour + 1 , 
            data["hora"].minute, 
            data["hora"].second, 
            data["hora"].microsecond
        )
        
        pedidos = pedido.objects.get_queryset().filter(hora__gte = data["hora"] , hora__lte = horafinal ) 
        
        if len(pedidos)>0:
            raise serializers.ValidationError("El pedido se cruza con otro")

        return super().validate(data)
