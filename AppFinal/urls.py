from django.urls import path    
from AppFinal import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    
    path('', views.inicio, name="inicio"),
    path('cliente', views.cliente, name="cliente"),
    path('celular', views.tuCelu, name="tuCelu"),
    path('leerCelular', views.leerCelular, name="leerCelular"),
    
    path('celulares/list', views.CeluList.as_view(), name='Listc'),
    path(r'detailcel/^(?P<pk>\d+)$', views.CeluDetalle.as_view(),name='Detailc'),
    path(r'^nuevocel$', views.CeluCreacion.as_view(), name='Newc'),
    path(r'^editarcel/(?P<pk>\d+)$', views.CeluUpdate.as_view(),name='Editc'),
    path(r'^borrarcel/(?P<pk>\d+)$', views.CeluDelete.as_view(),name='Deletec'),
    
    path('descuentos', views.descuentos, name='descuentos'),
    path('internet', views.internet, name= 'internet'),
    path('planes', views.planes, name="planes"),
    path('linea',views.newLinea, name="newLinea"),
    path('nuevocliente',views.nuevocliente, name="nuevocliente"),
    
    path('buscar/',views.buscar, name="buscar"),
    path('buscarCliente/',views.buscarCliente, name="buscarCliente"),
    path('leerClientes', views.leerClientes, name="LeerClientes"),
    path('eliminarCliente/<cliente_nombre>',views.eliminarCliente, name="EliminarCliente"),
    path('editarCliente/<cliente_nombre>', views.editarCliente, name="editarCliente"),
    
    
    path('cliente/list', views.ClienteList.as_view(),name='List'),
    path(r'^(?P<pk>\d+)$', views.ClienteDetalle.as_view(), name="detail"),
    path(r'^nuevos$',views.ClienteCreacion.as_view(),name='New'),
    path(r'^editar/(?P<pk>\d+)$',views.ClienteUpdate.as_view(),name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$',views.ClienteDelete.as_view(),name='Delete'),
   
   
    path('login', views.login_request, name='Login'),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppFinal/logout.html'), name='logout'),
    path('about', views.about, name='about'),
    path('editarPerfil', views.editarPerfil, name="editarPerfil"),
    
    
    ]
