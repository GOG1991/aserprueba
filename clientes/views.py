# -*- encoding: utf-8 -*-
from django.forms import ModelForm, TextInput , ModelChoiceField ,Select 
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.template.context import RequestContext
from django.views.generic import ListView
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from django.forms.models import inlineformset_factory as inlineform
from django.contrib.auth.decorators import login_required
import json

from braces.views import LoginRequiredMixin

from .models import clientes, reputacionesClientes, personasAutorizadas, reputaciones
from servicios.models import servicios
from .forms import clienteForm, reputacionesForm,PictureForm

'''
class ClientesListView(LoginRequiredMixin, ListView):
	login_url = '/'
	queryset = clientes.objects.order_by('-id')
	template_name='clientes.html'
	context_object_name = 'clientes'
	
	def get_context_data(self, **kwars):
		context = super(ClientesListView, self). get_context_data(**kwars)
		return context
'''
@login_required(login_url='/')
def clientesList(request):
	clientesl = list(clientes.objects.all())
	for cliente in clientesl:
		repuList = reputacionesClientes.objects.all().filter(cliente = cliente.id)
		try:
			lastReputacion = repuList[0]
		except IndexError:
			lastReputacion = 'null'
		if lastReputacion == 'null':
			print ('El cliente '+ str(cliente.nombre) +' no tiene una reputacion' )
		else:
			print ('El cliente '+ str(cliente.nombre) +' tiene una reputacion '+ str(lastReputacion.reputacion.nombre) )
		
	template = 'clientes.html'
	return render_to_response(template, context_instance = RequestContext(request,locals()))


def crear_cliente(request):
	if request.method == 'POST':
		formAddC = clienteForm(request.POST)
		if formAddC.is_valid():
			formAddC.save()
			return redirect('/clientes')
		else:
			form = formAddC
	else:
		form = clienteForm()
	return render(request, 'cliente_form.html', {'form': form})


@login_required(login_url='/')
def add_cliente(request):
	cliente = clientes()
	reputacionFormset = inlineform (clientes, reputacionesClientes,  can_delete = False, extra = 1, form = reputacionesForm)
	print ('Ya entre a la vista')
	if request.is_ajax():
		clienteform = clienteForm()
		repformset = reputacionFormset(instance = cliente)
		print ('Si viene por ajax')

	if request.method == 'POST' and request.is_ajax():
		clienteform = clienteForm(request.POST)
		print ('method POST')
		if clienteform.is_valid():
			clienteform.save()
			clienteid=clienteform.instance.pk
			nombre=clienteform.instance.nombre
			cliente = clientes.objects.get(pk = clienteid)
			data = {
				'id': clienteid,
				'nombre': nombre,
				}
			json_data = json.dumps(data)
			repformset = reputacionFormset(request.POST, instance = cliente)
			if repformset.is_valid:
				repformset.save()
			print ('Valido los dos formularios')
		else:
			print('algo anda mal');	
		return HttpResponse(json_data, content_type="application/json")
	else:
		clienteform = clienteForm(instance = cliente)
		repformset = reputacionFormset(instance = cliente)
	template = 'cliente_form.html'
	return render_to_response(template, context_instance = RequestContext(request, locals()))

#editar cliente con inlineformset
def addPic(request):
	if request.method == 'POST':
		cliente = clientes.objects.get(id = int(request.POST['id']))
		pictureform = PictureForm(request.POST,request.FILES , instance = cliente)
		if pictureform.is_valid():
			pictureform.save()
		return HttpResponseRedirect('/clientes/detaill_cliente/%d/'%cliente.id)

	else:
		HttpResponse('error consulte a su proveedor de software')	
	

def edit_clienteInline(request, id):
	cliente = clientes.objects.get(pk = id)
	print (cliente)
	form = clienteForm(instance = cliente)
	reputacionFormset = inlineform (clientes, reputacionesClientes,  can_delete = False, extra = 1, form = reputacionesForm)
	repformset = reputacionFormset(instance = cliente)
	print ('Hola')
	if request.method == 'POST':
		form = clienteForm(request.POST, instance = cliente)
		print ('POST')
		if form.is_valid():
			cliente = form.save(commit = False)
			repformset = reputacionFormset(request.POST, request.FILES, instance = cliente)
			if repformset.is_valid():
				cliente.save()
				repformset.save()
				return redirect ('/clientes')
			else:
				print ('repformset no valido')
		else:
			print ('clienteform no valido')
	else:
		form = clienteForm(instance = cliente)
		repformset = reputacionFormset(instance = cliente)
	template = 'form.html'
	return render_to_response(template, context_instance = RequestContext(request, locals()))


def edit_cliente(request, id):
	cliente = clientes.objects.get(pk = id)
	if request.method == 'POST':
		formEdit = clienteForm(request.POST, instance = cliente)
		if formEdit.is_valid():
			formEdit.save()
			return redirect('/clientes')
		else:
			form = formEdit
	else:
		form = clienteForm(instance = cliente)
	return render(request, 'edit_cliente.html', {'form': form})


def edit_cliente2(request, id):
	cliente = clientes.objects.get(pk = id)
	if request.method == 'POST':
		formEdit = clienteForm(request.POST, instance = cliente)
		if formEdit.is_valid():
			formEdit.save()
			return redirect('/clientes')
		else:
			form = formEdit
	else:
		form = clienteForm(instance = cliente)
	return render(request, 'edit_cliente.html', {'form': form})


@login_required(login_url='/')
def detaill_cliente(request,id):
	cliente = get_object_or_404(clientes, id = id)
	pictureform = PictureForm(instance = cliente)
	personasAuto = personasAutorizadas.objects.all().filter(cliente = cliente)
	reputaciones = reputacionesClientes.objects.all().filter(cliente = cliente)
	length = len(reputaciones)
	ultima = reputaciones[0]
	servicioC = servicios.objects.all().filter(cliente = cliente.id)
	template = 'detail_cliente.html'
	return render_to_response(template, context_instance = RequestContext(request, locals()))


def listaReputaciones(request,id):
	cliente = get_object_or_404(clientes, id = id)
	reputaciones = reputacionesClientes.objects.all().filter(cliente = cliente)
	template = 'list_reputaciones.html'
	return render_to_response(template, context_instance = RequestContext(request, locals()))


def listaRep(request):
	cliente = get_object_or_404(clientes , id = int(request.GET['id']))
	if request.is_ajax():
		template = 'list_reputaciones.html'
		reputaciones = reputacionesClientes.objects.all().filter(cliente = cliente)
		return render_to_response(template, context_instance = RequestContext(request, locals()))
	else:
		return HttpResponse('no hay datos')	
		

class reputacionesListView(LoginRequiredMixin, ListView):
	login_url = '/'
	model = clientes
	template_name='list_reputaciones.html'
	context_object_name = 'reputaciones'
	
	def get_context_data(self, **kwars):
		context = super(reputacionesListView, self). get_context_data(**kwars)
		return context


def load_cliente(request):
	if request.is_ajax():
		cliente = clientes.objects.get(pk = request.GET['id'])
	form = clienteForm(instance = cliente)
	reputacionFormset = inlineform (clientes, reputacionesClientes,  can_delete = False, extra = 1, form = reputacionesForm)
	repformset = reputacionFormset(instance = cliente)
	return render(request, 'form.html', {'form': form})	


def load_form_registro(request):
	if request.is_ajax():
		clienteform = clienteForm()
		print ('Entre a la vista load_form_registro')
	template = 'cliente_form.html'
	#return render_to_response(template, context_instance = RequestContext(request, locals()))
	return render(request , template , {'clienteform':clienteform})


def updateCliente(request, id):
	cliente = clientes.objects.get(pk = id)
	return render(request, 'clientes.html')

			 

