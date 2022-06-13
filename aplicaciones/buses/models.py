from django.db import models

# Create your models here.
class buses(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length= 80)
    placa = models.CharField(max_length= 80)
    tipo = models.CharField(max_length= 80)
    numero_de_puestos = models.CharField(max_length= 80)
    def __str__(self):
        return self.tipo