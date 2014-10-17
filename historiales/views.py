# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response,get_object_or_404
from django.template.context import RequestContext
from django.views.generic import ListView
from django.http import HttpResponse
import json

from .models import fallas, soluciones
from .forms import fallaForm, solucionForm
from servicios.models import detalleServicio


class fallasListView(ListView):
	queryset = fallas.objects.order_by('-id')
	template_name = 'selectFalla.html'
	context_object_name = 'fallas'


def add_falla(request):
	falla = fallas()
	fallaform = fallaForm()
	if request.method == 'POST' and request.is_ajax():
		print ('Entre a POST y ajax')
		fallaform = fallaForm(request.POST)
		if fallaform.is_valid():
			nuevafalla = fallaform.save()
			data = {
			'id':nuevafalla.id,
			'nombre': nuevafalla.nombre,
			}
			print(nuevafalla.id)
			json_data = json.dumps(data)
			return HttpResponse(json_data, content_type = "application/json")
		else:
			print('No sirvio')
	if request.is_ajax():
		print('Entre a ajax')
		fallaform = fallaForm()
		return render (request, 'falla_form.html', {'fallaform':fallaform})
	template = 'falla_form.html'
	return render_to_response(template, context_instance = RequestContext(request, locals()))


def add_solucion(request):
	solucion = soluciones()
	solucionform = solucionForm()
	template = 'sol_form.html'
	if request.method == 'POST' and request.is_ajax():
		print ('Entre')
		solucionform = solucionForm(request.POST)
		if solucionform.is_valid():
			nuevasol = solucionform.save()
	elif request.is_ajax():
		print('si entra pero vale mona en el ajax')
		solucionform = solucionForm()
		return render_to_response(template, context_instance = RequestContext(request, locals()))
	template = 'sol_form.html'
	return render_to_response(template, context_instance = RequestContext(request, locals()))


def detail_solucion(request):
	template = 'detailSol.html'
	if request.is_ajax():
		sol = get_object_or_404(soluciones, id = request.GET['id'])
	else:
		print ('pelas')
	return render_to_response (template, context_instance = RequestContext(request, locals()))

