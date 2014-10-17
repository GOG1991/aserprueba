# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.views.generic import ListView , TemplateView
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from braces.views import LoginRequiredMixin

from servicios.models import servicios
from estados.models import estados
from .forms import loginForm


def login(request):
	mens = ''
	if request.user.is_authenticated():
		return HttpResponseRedirect('home/')
	else:
		if request.method == 'POST':
			formLogin = loginForm(request.POST)
			if formLogin.is_valid():
				username = formLogin.cleaned_data['username']
				password = formLogin.cleaned_data['password']
				usuario = authenticate(username = username, password = password)
				if usuario is not None and usuario.is_active:
					auth_login(request,usuario)
					return HttpResponseRedirect('home/')
				else:
					mens = 'Usuario y/o password incorrectos'
			else:
				pass
		formLogin = loginForm()
		template = 'home/login.html'
		return render_to_response(template, context_instance = RequestContext(request, locals()))


class Home(TemplateView):
	#login_url = '/'
	model = servicios
	template_name ='home/index.html' 
	#context_object_name = 'servicios'
	
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(Home, self).dispatch(*args, **kwargs)
		#return context

"""
def listaServicio(request):
	serv = servicios.objects.filter()
"""

def estados(request):
	estado = estados.objects.all()
	return render(request,'home/estados.html',{'estados':estado})


def serviciosEdos(request):
	listaSer = list(servicios.objects.all().filter())	
