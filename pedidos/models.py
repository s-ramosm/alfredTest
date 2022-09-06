from django.db import models
from django.test import modify_settings
from conductores.models import conductor
# Create your models here.
class pedido(models.Model):
    
    lat = models.FloatField()
    lng = models.FloatField()
    conductor = models.ForeignKey(conductor, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()