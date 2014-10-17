# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, url, include
from django.contrib.auth.views import logout
from .views import Home, login


# URL de esta app.
urlpatterns = patterns('',
	url(r'^logout/$',logout , {'next_page': '/'}, name='logout'),
	url(r'^$', login, name='login'),
	#url(r'^home/$',Home.as_view(), name='home'),
	url(r'^home/$','servicios.views.Listaservicios', name='home'),
	#url(r'^estados/$', 'home.views.estados', name='estados'),
)