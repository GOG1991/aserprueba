# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from equipos.models import categorias

class fallas(models.Model):
	nombre = models.CharField(_('Nombre de la falla'), max_length=50)
	descripcion = models.TextField(_('Descripción de la falla'), help_text='Describa '+
		'detalladamente esta falla', null = True, blank = True)
	categoria = models.ManyToManyField(categorias, related_name = 'categoria de falla')

	def __str__(self):
		return self.nombre

	class Meta():
		verbose_name= _('Falla')
		verbose_name_plural= _('Fallas')


class soluciones(models.Model):
	nombre = models.CharField(_('Nombre de la solucion'), max_length=50)
	descripcion = models.TextField(_('Descripción de la solucion'), help_text='Describa det'+
		'alladamente esta solucion', null = True, blank = True)

	def __str__(self):
		return self.nombre

	class Meta():
		verbose_name = _('Solucion')
		verbose_name_plural = _('Soluciones')



