from contextvars import Context
import imp
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template import Template, Context
from AppFinal.models import Cliente, Celular, Linea
from AppFinal.forms import nuevoclienteform, nuevaLinea, celular

# Create your views here.


def inicio(request):
        
        return render(request,"AppFinal/inicio.html")

def cliente(request):
        
        return render(request,"AppFinal/cliente.html")


def nuevocliente(request):
    if request.method == 'POST':

        miFormulario = nuevoclienteform(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            cliente = Cliente(name=informacion['name'], lastname=informacion['lastname'], dni=informacion['dni'], fechaAlta=informacion['fechaAlta'], email=informacion['email'])
            cliente.save()

            return render(request, "AppFinal/inicio.html")

    else:

        miFormulario= nuevoclienteform()

    return render(request, "AppFinal/nuevocliente.html", {"miFormulario":miFormulario})

def newLinea(request):
        if request.method=='POST':
                miLinea=nuevaLinea(request.POST)
                print(miLinea)
                   
                if miLinea.is_valid:
                        info=miLinea.cleaned_data
                        linea=Linea(numero=info['numero'], minutos=info['minutos'], datosmb=info['datosmb'])
                        linea.save()
                        
                        return render(request,"AppFinal/inicio.html")
        else:
                miLinea=nuevaLinea()
        
        return render(request, "AppFinal/linea.html",{"miLinea":miLinea})  

def tuCelu(request):
        if request.method=='POST':
                miCelu=celular(request.POST)
                print(miCelu)
                
                if miCelu.is_valid:
                        info=miCelu.cleaned_data
                        cel=Celular(marca=info['marca'], modelo=info['modelo'], precio=info['precio'])      
                        cel.save()
                        
                        return render(request, "AppFinal/inicio.html")
        else:
                miCelu=celular()
        
        return render(request,"AppFinal/celular.html", {"miCelu":miCelu})                
        
def buscar(request):
        
        if request.GET["numero"]:
                
                numero=request.GET['numero']
                lineas=Linea.objects.filter(numero__icontains=numero)
                
                return render(request, "AppFinal/resultadobusqueda.html", {"lineas":lineas, "numero":numero})
        
        else:
                respuesta="No se encontro la linea"
        
        return HttpResponse(respuesta)                


def buscarCliente(request):
        
        if request.GET["dni"]:
                
                dni=request.GET['dni']
                clientes=Cliente.objects.filter(dni__icontains=dni)
                
                return render (request, "AppFinal/resultadoCliente.html", {"clientes":clientes, "dni":dni})
        
        else:
                respuesta="No es un cliente registrado"

        return HttpResponse(respuesta)