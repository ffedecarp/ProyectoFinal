from django.urls import path    
from AppFinal import views




urlpatterns = [
    
    path('', views.inicio, name="inicio"),
    path('cliente', views.cliente, name="cliente"),
    path('celular', views.tuCelu, name="tuCelu"),
    path('linea',views.newLinea, name="newLinea"),
    path('nuevocliente',views.nuevocliente, name="nuevocliente"),
    path('buscar/',views.buscar, name="buscar"),
    path('buscarCliente/',views.buscarCliente, name="buscarCliente"),
    
]