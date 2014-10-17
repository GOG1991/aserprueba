# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.views.generic import ListView , DetailView
from django.template.context import RequestContext
from django.db.models import Count , Sum
from django.forms.models import inlineformset_factory
from django.forms import ModelForm, TextInput , ModelChoiceField ,Select , CharField
from django.http import HttpResponse, StreamingHttpResponse
from django.http import HttpResponseRedirect
from django.utils.timezone import localtime
from django.contrib.auth.decorators import login_required
from  django.core.exceptions import MultipleObjectsReturned
import json

from braces.views import LoginRequiredMixin
from datetime import timedelta, datetime
from wkhtmltopdf.views import PDFTemplateView

import pytz

from .models import servicios, servicioTieneEstados, detalleServicio, servicioTieneTipoServicio, servicioTieneProducto, servicioTienePerfil , productos, condiciones
from .forms import registroServicio, servicioForm, detalleServicioForm, servicioTieneEstadosForm, servicioTieneTipoServicioForm, servicioProductoForm, servicioTecnicoForm, domicilioForm, cambioEstadoForm, solucionForm, servicioProd,productosForm,costoForm , cambioEdoFin,cambioGarantia
from clientes.forms import clienteForm
from estados.forms import movimientoForm
from clientes.models import clientes , reputacionesClientes, personasAutorizadas
from estados.models import movimientos, estados
from equipos.models import equipoTieneAccesorios ,equipos
# importamos las funciones del archivo functions
from .functions import solveList, posiblesSoluciones



class ClientesListView(ListView):
	#login_url = '/'
	queryset = clientes.objects.order_by('-id')
	template_name='selectCli.html'
	context_object_name = 'clientes'
	
	def get_context_data(self, **kwars):
		context = super(ClientesListView, self). get_context_data(**kwars)
		return context


def estadosServicios(request):
	edosServices = {}
	for es in servicioTieneEstados.objects.select_related('servicio','estado').all():
		edosServices.setdefault(es.servicio.id,[]).append(es.estado)

	for servicio in servicios.objects.all():
		print ('Folio ' + str(servicio.id))
		for estado in edosServices[servicio.id]:
			print ('Estado ' + str(estado.nombre))
	template = 'servicios.html'
	return render_to_response (template, context_instance = RequestContext(request, locals()))


def addProductos(request):
	formProd = productosForm()
	template = 'addProd.html'
	if request.is_ajax() and request.method == 'POST':
		formProd = 	productosForm(request.POST)
		if formProd.is_valid():
			formProd.save()
	return render_to_response (template, context_instance = RequestContext(request, locals()))


@login_required(login_url='/')
def add_service2(request):
	#cuando sean varios formsets hay que colocar prefijos
	status = 0
	val = 1
	objs = servicios.objects.first()
	if objs is not None:
		next_Folio = (int(objs.id)+1)
	else:
		next_Folio = 0
	detalleServicioFormset = inlineformset_factory(servicios, detalleServicio, extra = 1, can_delete = False, form = detalleServicioForm)
	estadosServicioFormset = inlineformset_factory(servicios, servicioTieneEstados, extra = 1, can_delete = False, form = servicioTieneEstadosForm)
	tiposervicioFormset = inlineformset_factory(servicios, servicioTieneTipoServicio, extra = 1, can_delete = False, form = servicioTieneTipoServicioForm)
	servicioTieneProductoFormset = inlineformset_factory(servicios, servicioTieneProducto, extra = 1, can_delete = False, form = servicioProductoForm)
	servicioTienePerfilFormset = inlineformset_factory(servicios, servicioTienePerfil, extra = 1, can_delete = False, form = servicioTecnicoForm)
	if request.method == 'POST':
		serviceForm = servicioForm(request.POST)
		if serviceForm.is_valid():
			servicio = serviceForm.save(commit = False)
			tiposerFormset = tiposervicioFormset(request.POST, instance = servicio)
			estadoFormset = estadosServicioFormset(request.POST, instance = servicio)
			detalleFormset = detalleServicioFormset(request.POST, instance =  servicio, prefix='fs1')
			tecnicoserFormset = servicioTienePerfilFormset (request.POST, instance = servicio)
			#productoFormset = servicioTieneProductoFormset (request.POST, instance = servicio)
			if tiposerFormset.is_valid() and estadoFormset.is_valid() and detalleFormset.is_valid() and tecnicoserFormset.is_valid():
				servicio.save()
				servicioid=servicio.id
				tiposerFormset.save()
				obj = estadoFormset.save(commit = False)
				for tecnico in obj:
					tecnico.perfil = request.user
					tecnico.save()
				detalleFormset.save()
				#mantFormset.save()
				tecnicoserFormset.save()
				#productoFormset.save()
				val = 1
				return HttpResponseRedirect('/servicios/reciboSer/%d/'%servicio.id)
			else:
				status = 1
		else:
			status = 2
	else:
		status = 0
		serviceForm = servicioForm()
		tiposerFormset = tiposervicioFormset()
		detalleFormset = detalleServicioFormset(prefix='fs1')
		estadoFormset = estadosServicioFormset()
		tecnicoserFormset = servicioTienePerfilFormset()
		productoFormset = servicioTieneProductoFormset()
	template = 'crearServicio.html'
	return render_to_response(template, context_instance = RequestContext(request, locals()))


@login_required(login_url='/')
def add_service_varios(request):
	status = 0
	objs = servicios.objects.last()
	print ( obj.id)
	next_Folio = 0
	detalleServicioFormset = inlineformset_factory(servicios, detalleServicio, extra = 1, can_delete = True, form = detalleServicioForm)
	estadosServicioFormset = inlineformset_factory(servicios, servicioTieneEstados, extra = 1, can_delete = False, form = servicioTieneEstadosForm)
	#tiposMantenimientoFormset = inlineform(servicios, servicioTieneTipoMant, extra = 1, can_delete = False, form = servicioTieneTipoMantForm)
	tiposervicioFormset = inlineformset_factory(servicios, servicioTieneTipoServicio, extra = 1, can_delete = False, form = servicioTieneTipoServicioForm)
	servicioTieneProductoFormset = inlineformset_factory(servicios, servicioTieneProducto, extra = 1, can_delete = False, form = servicioProductoForm)
	servicioTienePerfilFormset = inlineformset_factory(servicios, servicioTienePerfil, extra = 1, can_delete = False, form = servicioTecnicoForm)
	if request.method == 'POST':
		serviceForm = servicioForm(request.POST)
		if serviceForm.is_valid():
			servicio = serviceForm.save(commit = False)
			if 'add_equipo' in request.POST:
				#realizamos una copia de todos los datos que vienen por POST
				copia = request.POST.copy()
				#modificamos el campo TOTAL_FORM
				copia ['servicios detalle-TOTAL_FORMS'] = int(copia['servicios detalle-TOTAL_FORMS']) + 1
				detalleFormset = detalleServicioFormset(copia, instance = servicio)
				estadoFormset = estadosServicioFormset(request.POST, instance = servicio)
				tiposerFormset = tiposervicioFormset(request.POST, instance = servicio)
				#mantFormset = tiposMantenimientoFormset(request.POST, instance = servicio)
				tecnicoserFormset = servicioTienePerfilFormset(request.POST, instance = servicio)
				productoFormset = servicioTieneProductoFormset(request.POST, instance = servicio)
			elif 'submit' in request.POST:
				detalleFormset = detalleServicioFormset(request.POST, instance =  servicio)
				estadoFormset = estadosServicioFormset(request.POST, instance = servicio)
				tiposerFormset = tiposervicioFormset(request.POST, instance = servicio)
				#mantFormset = tiposMantenimientoFormset(request.POST, instance = servicio)
				tecnicoserFormset = servicioTienePerfilFormset(request.POST, instance = servicio)
				#productoFormset = servicioTieneProductoFormset(request.POST, instance = servicio)
				if tiposerFormset.is_valid() and estadoFormset.is_valid() and detalleFormset.is_valid() and tecnicoserFormset.is_valid():# and productoFormset.is_valid():
					servicio.save()
					servicioid=servicio.id
					tiposerFormset.save()
					obj = estadoFormset.save(commit = False)
					for tecnico in obj:
						tecnico.perfil = request.user
						tecnico.save()
					detalleFormset.save()
					tecnicoserFormset.save()
					#productoFormset.save()
					#return redirect ('/home')
					val = 1
					return HttpResponseRedirect('/servicios/reciboSer/%d/'%servicio.id )
				else:
					status = 1
			else:
				pass
		else:
			status = 2
	else:
		status = 0
		serviceForm = servicioForm()
		detalleFormset = detalleServicioFormset()
		tiposerFormset = tiposervicioFormset()
		estadoFormset = estadosServicioFormset()
		tecnicoserFormset = servicioTienePerfilFormset()
		#productoFormset = servicioTieneProductoFormset()
	template = 'crearServicio.html'
	return render_to_response(template, context_instance = RequestContext(request, locals()))


def add_service_ajax(request):
	detalleServicioFormset = inlineformset_factory(servicios, detalleServicio, extra = 1, can_delete = True, form = detalleServicioForm)
	estadosServicioFormset = inlineformset_factory(servicios, servicioTieneEstados, extra = 1, can_delete = False, form = servicioTieneEstadosForm)
	tiposervicioFormset = inlineformset_factory(servicios, servicioTieneTipoServicio, extra = 1, can_delete = False, form = servicioTieneTipoServicioForm)
	#servicioTieneProductoFormset = inlineformset_factory(servicios, servicioTieneProducto, extra = 1, can_delete = False, form = servicioProductoForm)
	servicioTienePerfilFormset = inlineformset_factory(servicios, servicioTienePerfil, extra = 1, can_delete = False, form = servicioTecnicoForm)
	if request.method == 'POST':
		serviceForm = servicioForm(request.POST)
		if serviceForm.is_valid():
			servicio = serviceForm.save(commit = False)
			if request.is_ajax():
				#realizamos una copia de todos los datos que vienen por POST
				copia = request.POST.copy()
				#modificamos el campo TOTAL_FORM
				copia ['servicios detalle-TOTAL_FORMS'] = int(copia['servicios detalle-TOTAL_FORMS']) + 1
				detalleFormset = detalleServicioFormset(copia, instance = servicio)
				estadoFormset = estadosServicioFormset(request.POST, instance = servicio)
				tiposerFormset = tiposervicioFormset(request.POST, instance = servicio)
				#mantFormset = tiposMantenimientoFormset(request.POST, instance = servicio)
				tecnicoserFormset = servicioTienePerfilFormset(request.POST, instance = servicio)
				#productoFormset = servicioTieneProductoFormset(request.POST, instance = servicio)
		else:
			print ('serviceForm no valido')

	template = 'addEquipos.html'
	return render_to_response(template, context_instance = RequestContext(request, locals()))


def selProd(request):
	formProd = servicioProductoForm()
	msj = ""
	if request.method == 'POST':
		print(request.POST['id'])
		servicio = servicios.objects.get(id = request.POST['id'])
		prod = servicioProductoForm(request.POST,instance = servicio)
		print (prod)
		if prod.is_valid():
			producto = prod.cleaned_data['producto']
			cantidad = prod.cleaned_data['cantidad']
			if servicioTieneProducto.objects.filter(servicio = servicio , producto = producto).exists():
				l = servicioTieneProducto.objects.get(servicio = servicio , producto = producto)
				precio = productos.objects.get(id = l.producto.id)
				precio = precio.precio
				subtotal = (precio * cantidad)
				l.subtotal = subtotal
				l.cantidad = cantidad
				msj = "modificada"
				l.save()

			else:
				prodAgregado = servicioTieneProducto.objects.create(servicio = servicio, producto = producto , cantidad = cantidad)
				precio = productos.objects.get(id = prodAgregado.producto.id)
				precio = precio.precio
				subtotal = (precio * cantidad)
				prodAgregado.subtotal = subtotal
				prodAgregado.save()					

			return HttpResponse(str(producto)+" <span class='active'> Cantidad "+str(msj)+str("</span>")+" "+str(cantidad))
	template = 'selprod.html'
	return render_to_response(template, context_instance = RequestContext(request, locals()))		
	

@login_required(login_url='/')
def detaillservice(request, id):
	servicio = get_object_or_404(servicios, id = id)
	listProd = list(servicioTieneProducto.objects.all().filter(servicio = servicio))
	listaestados = list(servicioTieneEstados.objects.all().filter(servicio = servicio))
	listatecnicos = list(servicioTienePerfil.objects.all().filter(servicio = servicio))
	listaTiposer = list(servicioTieneTipoServicio.objects.all().filter(servicio = servicio))
	listaTipoS = listaTiposer[0]
	lastEstado = listaestados[0]
	listadetalles = list(detalleServicio.objects.all().filter(servicio = servicio))
	edoForm = cambioEdoFin()
	garantia = cambioGarantia()
	sol =[]
	#totales en caso de existir
	totC = 0
	total = 0

	if servicio.costo_descuento != None:
		for i in listProd:
			print(i.producto.precio)
			total += i.subtotal
		if int(servicio.costo_descuento) > 0:
			desc = int(servicio.costo_descuento)/100
			totC = int(total+servicio.costo+servicio.costo_respaldo)
			totC = totC - (totC * desc)
		else:	
			totC = int(total+servicio.costo+servicio.costo_respaldo)
			
	#ciclo para conocer las fallas de los equipos
	for equipo in listadetalles:
		# asigno el resultado de la funcion a un diccionario
		d = solveList(equipo.falla.id)
		#obtengo los id's de las suluciones, que son las keys del diccionario
		keys = list(d.keys())
		#obtengo las veces que fue utilizada esa solucion para resolver el problema, que son los values del diccionario
		values = list(d.values())
		#llamamos a la funcion y le pasamos como parametros keys y values
		# la funcion nos retorna un diccionario con el nombre de la solucion y cuantas veces se utilizo en la falla
		ps = posiblesSoluciones(keys, values)
		#creamos una lista con todos los diccionarios que nos pueda retornar la funcion
		sol.append(ps)
	template = 'detailservice.html'
	return render_to_response(template, context_instance = RequestContext(request, locals()))


def detalleRecibo(request , id):
	servicio = get_object_or_404(servicios, id = id)
	listProd = list(servicioTieneProducto.objects.all().filter(servicio = servicio))
	listaestados = list(servicioTieneEstados.objects.all().filter(servicio = servicio))
	listatecnicos = list(servicioTienePerfil.objects.all().filter(servicio = servicio))
	listaTiposer = list(servicioTieneTipoServicio.objects.all().filter(servicio = servicio))
	listaTipoS = listaTiposer[0]
	lastEstado = listaestados[0]
	listadetalles = list(detalleServicio.objects.all().filter(servicio = servicio))
	listProd = list(servicioTieneProducto.objects.all().filter(servicio = servicio.id))
	totC = 0
	total = 0
	template = 'reciboCarta.html'
	if servicio.costo_descuento != None:
		for i in listProd:
			print(i.producto.precio)
			total += i.subtotal
		if int(servicio.costo_descuento) > 0:
			desc = int(servicio.costo_descuento)/100
			totC = int(total+servicio.costo+servicio.costo_respaldo)
			totC = totC - (totC * desc)
		else:	
			totC = int(total+servicio.costo+servicio.costo_respaldo)
	return render_to_response(template, context_instance = RequestContext(request, locals()))


@login_required(login_url='/')
def historialEstados(request,id):
	servicio = get_object_or_404(servicios, id = id)
	listaestados = list(servicioTieneEstados.objects.all().filter(servicio = servicio))
	template = 'historialEstados.html'

	return render_to_response(template, context_instance = RequestContext(request, locals()))


@login_required(login_url='/')
def historialEdos(request):
	template = 'historialEstados.html'
	if request.is_ajax():
		servicio = get_object_or_404(servicios, id = request.GET['id'])
		listaestados = list(servicioTieneEstados.objects.all().filter(servicio = servicio))
		return render_to_response(template, context_instance = RequestContext(request, locals()))
	return render_to_response(template, context_instance = RequestContext(request, locals()))	


@login_required(login_url='/')
def historialEquipos(request):
	equipo = get_object_or_404(equipos , id = request.GET['id'])
	if request.is_ajax():
		listaserv = list(detalleServicio.objects.all().filter(equipo = equipo.id))
		template = 'historialEquipos.html'
	return render_to_response(template, context_instance = RequestContext(request, locals()))


@login_required(login_url='/')
def cambioestado(request):
	if request.is_ajax() and request.method == 'POST':
		servicio = servicios.objects.get(id = request.POST['id'])
		cambEstado = cambioEstadoForm(request.POST, instance = servicio)
		if cambEstado.is_valid():
			try:
				estadobueno = int(request.POST['estado'])
				edo = estados.objects.get(id = estadobueno)
			except KeyError:
				estadobueno = None
			razonCambio = cambEstado.cleaned_data['razonCambio']
			if edo:
				newEstado = servicioTieneEstados.objects.create( servicio = servicio, estado = edo, razonCambio = razonCambio ,perfil = request.user)
				if estadobueno == 4:
					print (estadobueno)
					servicio.fechaTerminado = datetime.now()
					servicio.save()
			else:
				print ('Ocurrio un error... :(')	
			#return HttpResponseRedirect ('/servicios/detail_service/%d/'%servicio.id)
		return HttpResponse(edo)

	if request.is_ajax():
		servicio = int(request.GET['id'])
		listaestados = list(servicioTieneEstados.objects.all().filter(servicio = servicio))
		lastEstado = listaestados[0]
		estadosvalidos = list(movimientos.objects.all().filter(estado = lastEstado.estado.id))		
	cambEstado = cambioEstadoForm()
	template = 'cambioEstado.html'
	return render_to_response(template, context_instance = RequestContext(request, locals()))


def estadofin(request): # cambia el estado a entregado
	edo = 0
	val = 2
	if request.method == 'POST':
		servicio = servicios.objects.get(id = int(request.POST['idSv']))
		edoFin = cambioEdoFin(request.POST, instance = servicio)
		if edoFin.is_valid():
			try:
				estadobueno = request.POST['estado']
				edo = estados.objects.get(id = estadobueno)
			except KeyError:
				estadobueno = None
			razonCambio = edoFin.cleaned_data['razonCambio']
			if edo:
				newEstado = servicioTieneEstados.objects.create( servicio = servicio, estado = edo, razonCambio = razonCambio ,perfil = request.user)
				servicio.fechaEntregado = datetime.now()
				servicio.save()

			else:
				print ('Ocurrio un error... :(')	
			val = 2		
			return HttpResponseRedirect('/servicios/reciboSer/%d/'%servicio.id)
	return HttpResponse(edo)


@login_required(login_url='/')	
def salidaSer(request,id): # muestra formulario para la salida de servicioservicioTieneProducto
	edoForm = cambioEdoFin() 
	servicio = get_object_or_404(servicios, id = id)
	formSalida = costoForm()
	total = 0
	subt = []
	cliente = servicio.cliente.id
	personasauto = personasAutorizadas.objects.filter(cliente = cliente)
	if request.is_ajax() and request.method == 'POST':
		costos = costoForm(request.POST)
		if costos.is_valid:
			costos.save()
			return HttpResponse('costos agregados')
	else:	
	#lis = productos.objects.all().aggregate(total = Sum('precio'))
		listProd = list(servicioTieneProducto.objects.all().filter(servicio = servicio.id))
		for i in listProd:
			print(i.producto.precio)
			total += i.subtotal
			print ('total ',total)
			#print ()
		#totalserv =lis.objects.all().agregate(Sum('precio'))
		template = 'salidaservicio.html'
		return render_to_response(template, context_instance = RequestContext(request, locals()))


def costosSer(request): # cambia el estado a entregado y saca el costo
	edo = 0
	if request.is_ajax() and request.method == 'POST':
		servicio = servicios.objects.get(id = int(request.POST['id'])) 
		costos = costoForm(request.POST , instance = servicio)
		#edoFin = cambioEdoFin(request.POST, instance = servicio)
		if costos.is_valid:
			costos.save()
			#print('costo guardado')
			'''if edoFin.is_valid():
				try:
					estadobueno = request.POST['estado']
					edo = estados.objects.get(id = estadobueno)
				except KeyError:
					estadobueno = None
				razonCambio = edoFin.cleaned_data['razonCambio']
				if edo:
					newEstado = servicioTieneEstados.objects.create( servicio = servicio, estado = edo, razonCambio = razonCambio ,perfil = request.user)
					servicio.fechaEntregado = datetime.now()
					servicio.save()
					print('tambien agrego el estado')
			else:
				print ('Ocurrio un error... :(')	'''
		else:
			return HttpResponse('error ! consulte al proveedor de software')				
	return HttpResponse('costos agregados y estado entregado')


@login_required(login_url='/')
def Listaservicios(request):
	services = list(servicios.objects.all())
	lista = []
	edo = 0
	name = []
	lis = []
	for servicio in services:
		lEstados = list(servicioTieneEstados.objects.all().filter(servicio = servicio.id))
		lastEstado = lEstados[0]
		estado = lEstados[0]
		name.append(estado.estado.nombre)	
		if request.is_ajax():
			edo = int(request.GET['id'])
			if lastEstado.estado.id == edo:
				lista.append(servicio)
				if not lista:
					print ('No hay servicio en el estado')		
		else:
			lista = services
			lis = zip(lista,name)	

	lis = zip(lista,name)			

	template = 'home/index.html'
	return render_to_response (template, context_instance = RequestContext(request, locals()))


def filtroServicios(request):
	services = list(servicios.objects.all())
	if request.is_ajax():
		edo = int(request.GET['id'])
		name = ''
		lista = []
		for servicio in services:
			lEstados = list(servicioTieneEstados.objects.all().filter(servicio = servicio.id))
			lastEstado = lEstados[0]
			if lastEstado.estado.id == edo:
				lista.append(servicio)	
				name = lastEstado.estado.nombre
	template = 'listaservicios.html'
	return render_to_response (template, context_instance = RequestContext(request, locals()))	


def filtroTiposSer(request):
	services = list(servicios.objects.exclude(estado__id=5))
	if request.is_ajax():
		edo = int(request.GET['id'])
		name = []
		ban = 0
		lista = []
		lis = []
		for servicio in services:
			lTipos = list(servicioTieneTipoServicio.objects.all().filter(servicio = servicio.id))
			lastEstado = lTipos[0]
			lEstados = list(servicioTieneEstados.objects.all().filter(servicio = servicio.id))
			estado = lEstados[0]
			if lastEstado.tipo.id == edo:
				lista.append(servicio)
				name.append(estado.estado.nombre)
	lis = zip(lista,name)			
	template = 'listatiposer.html'
	return render_to_response (template, context_instance = RequestContext(request, locals()))		


def edoBall(request):
	servicioslist= list(servicios.objects.all())
	edo = 0
	if request.is_ajax():
		estado = int(request.GET['id'])
		if estado != 8:
			for servicio in servicioslist:
				listaEdos = list(servicioTieneEstados.objects.all().filter(servicio = servicio.id))
				lastEstado = listaEdos[0]
				if lastEstado.estado.id == estado:
					edo += 1
		else:
			edo = len(servicioslist)		

	return HttpResponse(edo)


def garantias(request):
	#fecha actual con el UTC
	hoy = datetime.now(pytz.timezone('America/Mexico_City'))
	servicio = get_object_or_404(servicios, id = request.GET['id'])
	ban = 0
	#fecha que se entrego el servicio
	if servicio.fechaEntregado:
		fechaEnt = localtime(servicio.fechaEntregado)
		#Ultimo dia de garantia
		udg = fechaEnt + timedelta(days=servicio.garantia)
		valido = hoy < udg
		#dias restantes
		restantes = udg - hoy
		horas = restantes.seconds / 3600
		ban = 1
	template = 'servicios.html'
	return render_to_response (template, context_instance = RequestContext(request, locals()))


def changeCondicion(request, id):
	servicio = get_object_or_404(servicios, id = id)
	condicion = condiciones.objects.get(id = 3)
	servicio.condicion = condicion
	servicio.save()
	return HttpResponseRedirect('/servicios/detail_service/%d/'%servicio.id)

def changeGarantia(request):
	if request.is_ajax() and request.method == 'POST':	
		servicio = servicios.objects.get(id = int(request.POST['id'])) 
		garantia = cambioGarantia(request.POST, instance = servicio)
		if garantia.is_valid:  
			garantia.save()	
		return HttpResponse(servicio.garantia)	


@login_required(login_url='/')
def add_solucion(request):
	solucionFormset = inlineformset_factory (servicios, detalleServicio, extra = 0, can_delete = False, form = solucionForm)
	if request.method == 'GET':
		servicio = get_object_or_404(servicios, id = request.GET['id'])
		
		solFormSet = solucionFormset(instance = servicio)
	if request.method == 'POST':
		servicio = servicios.objects.get(id = request.POST['id'])
		solFormSet = solucionFormset(request.POST, request.FILES, instance = servicio)
		if solFormSet.is_valid():
			solFormSet.save()
			return HttpResponse('')
	template = 'solucion.html'
	return render_to_response (template, context_instance = RequestContext(request, locals()))


def add_producto(request, id):
	servicio = get_object_or_404(servicios, id = id)
	print (servicio)
	form = servicioProd(instance = servicio)
	servicioTieneProductoFormset = inlineformset_factory(servicios, servicioTieneProducto, extra = 1, can_delete = True, form = servicioProductoForm)
	prodFormSet = servicioTieneProductoFormset(instance = servicio)
	print (prodFormSet)
	if request.method == 'POST':
		form = servicioProd(request.POST, instance = servicio)
		if form.is_valid():
			servicio = form.save(commit = False)
			prodFormSet = servicioTieneProductoFormset(request.POST, request.FILES, instance = servicio)
			if prodFormSet.is_valid():
				servicio.save()
				prodFormSet.save()
	template = 'producto.html'
	return render_to_response (template, context_instance = RequestContext(request, locals()))


class Imprimir(PDFTemplateView):
	filename = "mipdf.pdf"
	template_name = "recibo.html"
	show_content_in_browser = True
	cmd_options = {
		'margin-top': 5,
		'page-size':'A6',
	}

	def get_context_data(self, **kwargs):
		context = super(Imprimir , self).get_context_data(**kwargs)
		context['servicio'] = servicios.objects.get(pk = kwargs['pk'])
		return context


def Print(request,id):
	servicio = get_object_or_404(servicios, id = id)
	template = 'reciboCarta.html'
	return render_to_response (template, context_instance = RequestContext(request, locals()))


@login_required(login_url='/')
def reciboSer(request,id):
	idval = id
	template = 'reciboSer.html'
	return render_to_response (template, context_instance = RequestContext(request, locals()))


def reciboSerPrint(request,id):
	servicio = get_object_or_404(servicios, id = id)
	accesorios = []
	listProd = list(servicioTieneProducto.objects.all().filter(servicio = servicio))
	listaestados = list(servicioTieneEstados.objects.all().filter(servicio = servicio))
	listatecnicos = list(servicioTienePerfil.objects.all().filter(servicio = servicio))
	listaTiposer = list(servicioTieneTipoServicio.objects.all().filter(servicio = servicio))
	listaTipoS = listaTiposer[0]
	lastEstado = listaestados[0]
	listadetalles = list(detalleServicio.objects.all().filter(servicio = servicio))
	listProd = list(servicioTieneProducto.objects.all().filter(servicio = servicio.id))
	for i in listProd:
		total += i.producto.precio
	for e in listadetalles:
		accesorios.append(equipoTieneAccesorios.objects.filter(equipo = e.equipo))
	print(accesorios)	
	#accesorios = list(equipoTieneAccesorios.objects.filter(equipo = e.equipo))
	template = 'printR.html'
	return render_to_response(template, context_instance = RequestContext(request, locals()))
