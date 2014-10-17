# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, url, include

# URL de esta app.
urlpatterns = patterns('historiales.views',
	url(r'^add_falla/$', 'add_falla', name = 'addfalla'),
	url(r'^add_sol/$', 'add_solucion', name = 'addsol'),
	url(r'^detail_solucion/$', 'detail_solucion', name = 'detailsolucion'),
)