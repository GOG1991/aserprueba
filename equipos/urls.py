# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, url, include

# URL de esta app.
urlpatterns = patterns('',
	url(r'^add_equipo/$','equipos.views.add_equipo',name = 'addequipo'),
	url(r'update/(\d+)/$', 'equipos.views.update', name = 'update'),
	url(r'updateacc/$', 'equipos.views.updateacc', name = 'update'),
	url(r'^detail/(\d+)/$', 'equipos.views.listaAccesorios', name = 'detaileq'),
	url(r'^listac/$', 'equipos.views.listAccesorios', name = 'detaileq'),
	url(r'^filtroE/$', 'equipos.views.filtroEquipos', name = 'filtroE'),
)