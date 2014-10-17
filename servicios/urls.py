# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, url, include
#from .views import Index
from .views import ClientesListView , Imprimir , Print
from equipos.views import EquiposListView
from historiales.views import fallasListView


# URL de esta app.
urlpatterns = patterns('servicios.views',
	url(r'^clientes/$',ClientesListView.as_view(),name ='listaClientes'),
	url(r'^equipos/$',EquiposListView.as_view(), name = 'listaEquipos' ),
	url(r'^fallas/$', fallasListView.as_view(), name = 'listaFallas' ),
	url(r'^conteog/$','garantias'),
	#url(r'^contEdos/$','edoBall'),
	url(r'^conteo/$','Listaservicios'),
	url(r'^contEdos/$','edoBall', name = 'contball'),
	url(r'^add_service/$', 'add_service2', name = 'addService'),
	url(r'^add_serviceajax/$', 'add_service_ajax', name = 'addServiceajax'),
	url(r'^detail_service/(\d+)/$', 'detaillservice', name = 'detaillservice'),
	url(r'^detail_service/estados/(\d+)/$', 'historialEstados', name = 'estados'),
	url(r'^detail_equipo/$', 'historialEquipos', name = 'hisequi'),
	url(r'^detail_service/estados/$', 'historialEdos', name = 'edos'),
	#url(r'^detail_service/cambio_edo/(\d+)/$', 'cambioestado', name = 'cambioedo'),
	url(r'^detail_servic/cambio_edo/$', 'cambioestado', name = 'cambioedo'),
	url(r'^estadofin/$', 'estadofin', name = 'estadofin'),
	url(r'^selprod/$', 'selProd', name = 'selprod'),
	url(r'^solucion/$','add_solucion',name = 'addSolucion'),
	url(r'^costos/$','costosSer',name = 'costoServ'),
	url(r'^add_productos/$','addProductos',name = 'addProd'),
	url(r'^detail_service/salidaserv/(\d+)/$', 'salidaSer', name = 'salidaservice'),
	#url(r'^filtro/(\d+)/$', 'filtroServicios', name = 'filtroServicios'),
	url(r'^filtro/$', 'filtroServicios', name = 'filtroServicios'),
	url(r'^filtroTiposSer/$', 'filtroTiposSer', name = 'filtroTServ'),
	url(r'^imprimir/(?P<pk>[\d]+)/$',Imprimir.as_view(),name= 'imprimir'),
	url(r'^print/(\d+)/$','Print',name= 'print'),
	url(r'^detailrecibo/(\d+)/$', 'detalleRecibo', name = 'detalleRecibo'),
	url(r'^reciboSer/(\d+)/$', 'reciboSer', name = 'reciboSer'),
	url(r'^reciboSerPrint/(\d+)/$', 'reciboSerPrint', name = 'reciboSerPrint'),
	url(r'^garantia/(\d+)/$', 'changeCondicion', name = 'cambiarcon'),
	url(r'^cambiarGar/$', 'changeGarantia', name = 'changeGarantia'),

)