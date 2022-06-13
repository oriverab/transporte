from django.db import models

# Create your models here.
class usuarios(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length= 80)
    apellido = models.CharField(max_length= 80)
    correo = models.CharField(max_length= 80)
    contraseña = models.CharField(max_length= 80)

def __str__(self):
        return self.nombre