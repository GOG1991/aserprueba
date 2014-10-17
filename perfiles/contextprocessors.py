# -*- encoding: utf-8 -*-
from servicios.models import servicioTienePerfil, servicioTieneEstados

"""
def serperfil(request):
	'''
	Funcion para saber cuantos servicios tiene el perfil que inicio sesion

	'''
	# Hacemos esta validacion para restar una unidad al id del usuario que esta en la sesion
	# porque el primer user va a ser el superusario y no va a tener el perfil
	if request.user.id != None:
		id = (request.user.id - 1)
	else:
		id = None
	lservicios = list(servicioTienePerfil.objects.all().filter(perfil = id))
	lista = []
	cont = 0
	serv = []
	for servicio in lservicios:
		listaEdos = list(servicioTieneEstados.objects.all().filter(servicio = servicio.id))
		lastEstado = listaEdos[0]
		#if lastEstado.estado.id != 4 and lastEstado.estado.id != 5:
		if lastEstado.estado.id == 1:	
			cont += 1
			lista.append(servicio)
	return {'cont': cont, 'lservicios': lista,}
"""

