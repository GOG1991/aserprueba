# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, url, include

#from .views import ClientesListView


urlpatterns = patterns('',
	url(r'^$','clientes.views.clientesList',name='listaClientes'),
	#url(r'^$','clientes.views.clientesList',name='listaClientes'),
	url(r'^edit_cliente/(\d+)/$', 'clientes.views.edit_cliente', name = 'editCliente'),
	url(r'^detaill_cliente/(\d+)/$', 'clientes.views.detaill_cliente', name = 'detaill_cliente'),
	url(r'^detaill_cliente/reputaciones/(\d+)/$', 'clientes.views.listaReputaciones', name = 'hisrep'),
	url(r'^add_cliente/$', 'clientes.views.add_cliente', name='addCliente'),
	url(r'^load_cliente/$', 'clientes.views.load_cliente', name="load"),
	url(r'^load_form_registro/$', 'clientes.views.load_form_registro', name="registro"),
	url(r'^update_cliente/(\d+)/$', 'clientes.views.updateCliente', name="update"),
	url(r'^lisrep/$', 'clientes.views.listaRep', name = 'lisrep'),
	url(r'^addPic/$', 'clientes.views.addPic', name = 'addPic'),

)