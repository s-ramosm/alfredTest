from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response 
from rest_framework.decorators import action
#Model 
from .models import conductor
from pedidos.models import pedido
#Serializer
from .serializers import conductorSerializer
#Util functions
from .utils import distancia_entre_dos_puntos




import datetime
import requests



class conductoresViewSet(ModelViewSet):
    serializer_class = conductorSerializer
    queryset = conductor.objects.all()

    @action(detail=False, methods=['post'])
    def conductor_cerca(self, request,*arg,**kwargs):
        
        geoData = requests.get("https://gist.githubusercontent.com/jeithc/96681e4ac7e2b99cfe9a08ebc093787c/raw/632ca4fc3ffe77b558f467beee66f10470649bb4/points.json")
        geoData = geoData.json()
        
        lat,lng = request.data.get("lat",0) , request.data.get("lng",0)
        fecha = request.data.get("fecha")
        hora = request.data.get("hora")

        #Calculando la distancias entre el punto y los conductores
        for conductor in geoData["alfreds"]:
            conductor["distancia"] = distancia_entre_dos_puntos((int(lat),int(lng)), (int(conductor["lat"]), int(conductor["lng"])))
        
        #Ordenando por distancia
        geoData["alfreds"] =  sorted(geoData["alfreds"], key=lambda item: item["distancia"])


        #Calculando hora final del pedido 
        hora = datetime.datetime.strptime(hora, '%H:%M:%S').time()
        horafinal = datetime.time(
            hora.hour + 1 , 
            hora.minute, 
            hora.second, 
            hora.microsecond
        )

        response = []
        #Descartando conductores con pedidos en rengo de solicitud
        for conductor in geoData["alfreds"]:
            pedidos = pedido.objects.get_queryset().filter(
                conductor = conductor["id"],
                fecha =fecha, hora__gte = hora, 
                hora__lte =horafinal 
                )
            
            if len(pedidos) ==0:
                response.append(conductor)


        return Response(response)   


