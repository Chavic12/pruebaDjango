from django.db import models

class Adopcion( models.Model ):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    cedula = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30)
    def __str__(self):
        return self.nombres
   
   
