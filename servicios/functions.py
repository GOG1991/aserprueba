# -*- encoding: utf-8 -*-
from .models import detalleServicio
from historiales.models import fallas, soluciones
import operator

def solveList(idf):
	#creamos una lista con los servicios que tenga la falla que se recive como argumento
	soldet = list(detalleServicio.objects.all().filter(falla = idf))
	idsol = []
	for sol in soldet:
		#creamos una lista con todos ids de las soluciones a partir de la primera lista
		idsol.append(sol.solucion.id)
	#creamos un diccionario con las soluciones y el numero que fueron soluciones para ese problema
	counter = dict()
	for k in idsol:
		counter.setdefault(k,0)
		counter[k] += 1
	return counter
	#mas info de esta funcion evanmuehlhausen.com/simple-counters-in-python-with-benchmarks/


def posiblesSoluciones(keys,values):
	lsolves = []
	for k, v in zip(keys, values):
		#obtenemos las soluciones 
		des = soluciones.objects.get(id = k)
		#creamos una lista con los objetos de las soluciones
		lsolves.append(des)
	#creamos un diccionario con la informacion de la lista de las soluciones como llave y el value son las veces que se utilizo esa solucion
	dicsol = dict(zip(lsolves, values))
	return dicsol