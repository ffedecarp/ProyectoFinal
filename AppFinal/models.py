import email
from django.db import models
import datetime 
from django.contrib.auth.models import User

# Create your models here.


class Cliente(models.Model):
    name=models.CharField(max_length=40)
    lastname=models.CharField(max_length=50)
    dni=models.IntegerField()
    fechaAlta=models.DateField()
    email=models.EmailField()

    def __str__(self):
        return f"Nombre:{self.name} - Apellido:{self.lastname} - DNI:{self.dni} - Fecha de alta:{self.fechaAlta} - Email:{self.email}"

 
class Linea(models.Model):
    numero=models.IntegerField()
    minutos=models.IntegerField()
    datosmb=models.FloatField()
    
    def __str__(self):
        return f"Numero:{self.numero} - Minutos:{self.minutos} - Datos:{self.datosmb}"

class Celular(models.Model):
    marca=models.CharField(max_length=40)
    modelo=models.CharField(max_length=40)
    precio=models.FloatField()
    
    def __str__(self):
        return f"Marca:{self.marca} - Modelo:{self.modelo} - Precio:{self.precio}"
    

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='avatares', null=True, blank=True)    