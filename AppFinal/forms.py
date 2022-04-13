from unittest.util import _MAX_LENGTH
from django import forms
import datetime

class nuevoclienteform(forms.Form):
    
    name=forms.CharField(max_length=40)
    lastname=forms.CharField(max_length=40)
    dni=forms.IntegerField()
    fechaAlta=forms.DateField ()
    email=forms.EmailField ()
    
class nuevaLinea(forms.Form):
    
    numero=forms.IntegerField()
    minutos=forms.IntegerField()
    datosmb=forms.FloatField()

class celular(forms.Form):
    
    marca=forms.CharField(max_length=40)
    modelo=forms.CharField(max_length=40)
    precio=forms.FloatField()


    