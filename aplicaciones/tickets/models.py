from django.db import models
from aplicaciones.principal.models import usuarios
from aplicaciones.buses.models import buses
from aplicaciones.rutas.models import rutas

class tickets(models.Model):
    id = models.AutoField(primary_key= True)
    fecha = models.CharField(max_length= 80)
    puestos = models.IntegerField(max_length=80)
    usuarios_id = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    buses_id = models.ForeignKey(buses, on_delete=models.CASCADE)
    rutas_id = models.ForeignKey(rutas, on_delete=models.CASCADE)
    