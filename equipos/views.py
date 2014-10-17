# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template.context import RequestContext
from django.forms.models import inlineformset_factory as inlineform
from django.forms.formsets import formset_factory
from django.views.generic import ListView
from django.http import HttpResponse
import json

from .models import equipos, equipoTieneAccesorios
from servicios.models import servicios
from .forms import equipoForm, equipoaccesorioForm
from servicios.models import detalleServicio


class EquiposListView(ListView):
	queryset = equipos.objects.order_by('-id')
	template_name = 'selectEqui.html'
	context_object_name = 'equipos'


def filtroEquipos(request):
	services = list(servicios.objects.all().filter(cliente = request.GET['id']).order_by('equipo').distinct('equipo'))
	lista = []
	for servicio in services:
		listaDet = detalleServicio.objects.all().filter(servicio = servicio.id)
		lista.append(listaDet)
	
	'''if not lista:
		ultimoequipo = equipos.objects.last()
		print (ultimoequipo)'''

	template = 'filterequipo.html'
	return render_to_response(template, context_instance = RequestContext(request, locals()))


def add_equipo(request):
	equipo = equipos()
	equipoaccesorioFormset = inlineform (equipos, equipoTieneAccesorios, can_delete = False, extra = 1, form = equipoaccesorioForm)
	
	if request.is_ajax():
		equipoform = equipoForm()
		acceformset = equipoaccesorioFormset(instance = equipo)
		print ('Entre a add_equipo si la peticion viene por ajax')

	if request.method == 'POST':
		equipoform = equipoForm(request.POST)
		if equipoform.is_valid():
			equipo = equipoform.save(commit = False)
			acceformset = equipoaccesorioFormset(request.POST, request.FILES, instance = equipo)
			if acceformset.is_valid():
				equipo.save()
				data = {
				'id': equipo.pk,
				'categoria': equipo.categoria.nombre,
				'categoriapk':equipo.categoria.pk,
				'noserie': equipo.noserie,
				'modelo':equipo.modelo,
				}
				json_data = json.dumps(data)
				acceformset.save()
				print('post')
				return HttpResponse(json_data, content_type="application/json")
			else:
				print ('formset no valido')
		else:
			print ('formulario de equipo no valido')

	else:
		equipoform = equipoForm()
		acceformset = equipoaccesorioFormset()
		print('cargue la modal')

		
	template = 'equipo_form.html'
	return render_to_response(template, context_instance = RequestContext(request, locals()))


def listaAccesorios(request, id):
	equipo = get_object_or_404(equipos, id = id)
	listac = list(equipoTieneAccesorios.objects.all().filter(equipo = equipo))
	listaser = list(detalleServicio.objects.all().filter(equipo = equipo))
	template = 'pset.html'
	return render_to_response(template, context_instance = RequestContext(request, locals()))


def listAccesorios(request):
	equipo = int(request.GET['id'])
	listac = list(equipoTieneAccesorios.objects.all().filter(equipo = equipo))
	template = 'pset.html'
	return render_to_response(template, context_instance = RequestContext(request, locals()))


def update(request,id):
	equipo = get_object_or_404(equipos, pk = id )
	form = equipoForm(instance = equipo)
	eformset = inlineform (equipos, equipoTieneAccesorios, can_delete = True, extra = 1, form = equipoaccesorioForm)
	eq_formset = eformset(instance = equipo)
	if request.method == 'POST':
		form = equipoForm(request.POST, instance = equipo)
		if form.is_valid():
			equipo = form.save(commit = False)
			eq_formset = eformset(request.POST, request.FILES, instance = equipo)
			if eq_formset.is_valid():
				equipo.save()
				eq_formset.save()
				# No retorno nada hasta ver como le vamos a hacer
	return render (request, "formeq.html", {'form': form, 'eq_formset': eq_formset})	


def updateacc(request):
	if request.is_ajax() and request.method == 'GET':
		equipo = get_object_or_404(equipos, pk = request.GET['id'])
		form = equipoForm(instance = equipo)
		eformset = inlineform (equipos, equipoTieneAccesorios, can_delete = True, extra = 1, form = equipoaccesorioForm)
		eq_formset = eformset(instance = equipo)
		return render (request, "formeq.html", {'form': form, 'eq_formset': eq_formset})
	elif request.is_ajax() and request.method == 'POST':
		equipo = equipos.objects.get(id = int(request.POST['txtidEa']))	
		form = equipoForm(request.POST, instance = equipo)
		eformset = inlineform (equipos, equipoTieneAccesorios, can_delete = True, extra = 1, form = equipoaccesorioForm)
		if form.is_valid():
			equipo = form.save(commit = False)
			eq_formset = eformset(request.POST, request.FILES, instance = equipo)
			if eq_formset.is_valid():
				equipo.save()
				eq_formset.save()

				return HttpResponse('echo')