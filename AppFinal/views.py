from contextvars import Context
import imp
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template import Template, Context
from AppFinal.models import Cliente, Celular, Linea
from AppFinal.forms import nuevoclienteform

# Create your views here.


def inicio(request):
        
        return render(request,"AppFinal/inicio.html")

def cliente(request):
        
        return render(request,"AppFinal/cliente.html")

def celular (request):
        
        return render(request,"AppFinal/celular.html")

def linea(request):
        
        return render(request,"AppFinal/linea.html")

# def NuevoCliente(request):
        
#         return render(request,"AppFinal/nuevocliente.html")

def nuevocliente(request):
    if request.method == 'POST':

        miFormulario = nuevoclienteform(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            cliente = Cliente(nOOOOOOOMBRE=informacion['name'], lastname=informacion['Apellido'], dni=informacion['DNI'], ncliente=informacion['N° Cliente'], fechaAlta=informacion['Fecha de Alta'], email=informacion['E-Mail'])
            cliente.save()

            return render(request, "AppFinal/inicio.html")

    else:

        miFormulario= nuevoclienteform()

    return render(request, "AppFinal/nuevocliente.html", {"miFormulario":miFormulario})