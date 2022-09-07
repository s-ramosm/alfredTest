from django.db import models
from django.test import modify_settings
from conductores.models import conductor
# Create your models here.
class pedido(models.Model):
    
    lat_inicial = models.FloatField()
    lng_inicial = models.FloatField()

    lat_final = models.FloatField()
    lng_final = models.FloatField()

    conductor = models.ForeignKey(conductor, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()