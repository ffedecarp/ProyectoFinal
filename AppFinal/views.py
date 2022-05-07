from ast import Del
from contextvars import Context
from dataclasses import fields
import imp
from unicodedata import name
import django
from typing import List
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from django.template import Template, Context
from AppFinal.models import Cliente, Celular, Linea, Avatar
from AppFinal.forms import nuevoclienteform, nuevaLinea, celular, UserRegisterForm, UserEditForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



def inicio(request):
        
       avatares = Avatar.objects.filter(user=request.user.id)
       return render(request, "AppFinal/inicio.html" , {"url": avatares[0].imagen.url})

def cliente(request):
        
        return render(request,"AppFinal/cliente.html")

def planes(request):
        return render(request,"AppFinal/planes.html")

def internet(request):
        return render(request, "AppFinal/internet.html")

def descuentos(request):
        return render(request, "AppFinal/descuentos.html")

def inicio(request):
        
        return render(request,"AppFinal/inicio.html")

def cliente(request):
        
        return render(request,"AppFinal/cliente.html")

def leerCelular(request):
        celulares=Celular.objects.all()
        contexto={"celulares":celulares}
        return render(request, "AppFinal/leerCelular.html",contexto)


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

@login_required
def buscarCliente(request):
        
        if request.GET["dni"]:
                
                dni=request.GET['dni']
                clientes=Cliente.objects.filter(dni__icontains=dni)
                
                return render (request, "AppFinal/resultadoCliente.html", {"clientes":clientes, "dni":dni})
        
        else:
                respuesta="No es un cliente registrado"

        return HttpResponse(respuesta)


@login_required
def leerClientes (request):
        
        clientes=Cliente.objects.all()
        
        contexto ={"clientes":clientes}
        
        return render(request, "AppFinal/leerClientes.html", contexto)

@login_required
def eliminarCliente(request,cliente_nombre):
        clientes=Cliente.objects.get(name=cliente_nombre)
        clientes.delete()
        
        clientes=Cliente.objects.all()
        contexto={"clientes":clientes}
        
        return render(request,"AppFinal/leerClientes.html", contexto)

@login_required
def editarCliente(request,cliente_nombre):
                cliente=Cliente.objects.get(name=cliente_nombre)
                
                if request.method == 'POST':               
                       
                        miFormulario=nuevoclienteform(request.POST)
                        
                        print(miFormulario)
                        
                        if miFormulario.is_valid:
                              
                                informacion=miFormulario.cleaned_data
                                
                                cliente.name=informacion['name']           
                                cliente.lastname=informacion['lastname']
                                cliente.dni=informacion['dni']
                                cliente.fechaAlta=informacion['fechaAlta']
                                cliente.email=informacion['email']        
                                cliente.save()
                                return render (request, "AppFinal/inicio.html")
                else:
                
                        miFormulario=nuevoclienteform(initial={'name':cliente.name,'lastname':cliente.lastname,'dni':cliente.dni, 'fechaAlta':cliente.fechaAlta, 'email':cliente.email})
               
                return render (request,"AppFinal/editarCliente.html",{"miFormulario":miFormulario,"cliente_nombre":cliente_nombre})                               

def leerCelular(request):
        celulares=Celular.objects.all()
        contexto={"celulares":celulares}
        return render(request, "AppFinal/leerCelular.html",contexto)


def about (request):
        return render (request, "AppFinal/about.html")


@login_required
def editarPerfil(request):
        usuario=request.user
        
        if request.method=='POST':
                miFormulario=UserEditForm(request.POST)
                if miFormulario.is_valid:
                        
                        informacion=miFormulario.cleaned_data
                        
                        usuario.email=informacion['email']
                        usuario.password1=informacion['password1']
                        usuario.password2=informacion['password1']
                        usuario.save()
                        
                        return render(request, "AppFinal/inicio.html")
                
        else:
                miFormulario=UserEditForm(initial={'email':usuario.email})
                
        return render(request, "AppFinal/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})
                
        
class ClienteList(ListView):
        
        model=Cliente
        template_name="AppFinal/cliente_list.html"

class ClienteDetalle(DetailView):
        
        model=Cliente
        template_name="AppFinal/cliente_detalle.html"

class ClienteCreacion(CreateView):
        
        model=Cliente
        success_url="/AppFinal/cliente/list"
        fields=['name', 'lastname', 'dni', 'fechaAlta', 'email']

class ClienteUpdate(UpdateView):
        
        model=Cliente
        success_url = "/AppFinal/cliente/list"             
        fields=['name', 'lastname', 'dni', 'fechaAlta', 'email']

class ClienteDelete(DeleteView):
        
        model=Cliente
        success_url="/AppFinal/cliente/list"

class CeluList(ListView):
        model=Celular
        template_name="AppFinal/celulares_list.html"

class CeluDetalle(DetailView):
        model=Celular
        template_name="AppFinal/celulares_detalle.html"

class CeluCreacion(CreateView):
        model=Celular
        success_url="/AppFinal/celulares/list"
        fields=['marca','modelo','precio']

class CeluUpdate(UpdateView):
        model=Celular
        success_url="/AppFinal/celulares/list"
        fields=['marca','modelo','precio']

class CeluDelete(DeleteView):
        model=Celular
        success_url="/AppFinal/celulares/list"        
        
def login_request(request):
        
        if request.method=="POST":
                form = AuthenticationForm(request, data = request.POST)
                
                if form.is_valid():
                        usuario= form.cleaned_data.get ('username')
                        contra=form.cleaned_data.get('password')
                        
                        user=authenticate(username=usuario, password=contra)
                        print("antes del if user")
                        if user is not None:
                                login (request, user)
                                print("adentro del is not none")
                                messages.success(request, f'Bienvenido {usuario}')
                                return render (request, "AppFinal/inicio.html")
                        else:   
                                print("adentro del else user")
                                messages.success(request, f'Error, Datos incorrectos')
                                return render(request,"AppFinal/inicio.html")
                
                else:   
                        messages.success(request, f'Error , formulario erroneo')
                        return render (request,"AppFinal/inicio.html")
        
        form=AuthenticationForm()
        print("afuera del loguin")
        return render(request,"AppFinal/login.html", {'form':form})

def register (request):
        if request.method == 'POST':
                #form= UserCreationForm(request.POST)
                form= UserRegisterForm(request.POST)
                if form.is_valid():
                        username=form.cleaned_data['username']
                        form.save()
                        messages.success(request, f'Usuario {username} creado correctamente')
                        return render (request, "AppFinal/inicio.html")
        else:
                #form = UserCreationForm()
                form = UserRegisterForm()
        return render(request, "AppFinal/registro.html", {"form":form})