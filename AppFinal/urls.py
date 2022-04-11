from django.urls import path    
from AppFinal import views



urlpatterns = [
    
    path('', views.inicio, name="inicio"),
    path('cliente', views.cliente, name="cliente"),
    path('celular', views.celular, name="celular"),
    path('linea',views.linea, name="linea"),
    path('nuevocliente',views.nuevocliente, name="nuevocliente"),
   
    
]