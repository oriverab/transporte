from django.db import models

class rutas(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length= 80)
    ciudad_origen = models.CharField(max_length= 80)
    ciudad_destino = models.CharField(max_length= 80)
    

 
def __str__(self):
        return f'{self.ciudad_origen} -> {self.ciudad_destino}'   