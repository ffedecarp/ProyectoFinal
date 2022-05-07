from dataclasses import field, fields
import email
from unittest.util import _MAX_LENGTH
from django import forms
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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

class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields= ['username','email', 'password1', 'password2']
        #saca los mensajes de ayuda
        help_texts= {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email=forms.EmailField(label="Modificar E-mail")
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=['email','password1','password2']
        help_texts={k:"" for k in fields}    


    