import email
from django.db import models
import datetime 


# Create your models here.


class Cliente(models.Model):
    name=models.CharField(max_length=40)
    lastname=models.CharField(max_length=50)
    dni=models.IntegerField()
    fechaAlta=models.DateField()
    email=models.EmailField()

 
class Linea(models.Model):
    numero=models.IntegerField()
    minutos=models.IntegerField()
    datosmb=models.FloatField()
    

class Celular(models.Model):
    marca=models.CharField(max_length=40)
    modelo=models.CharField(max_length=40)
    precio=models.FloatField()