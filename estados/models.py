# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class estados(models.Model):
	nombre = models.CharField(_('Nombre del estado'), max_length = 40)
	descripcion = models.CharField(_('Descripcion del estado'), max_length = 100, 
		null = True, blank = True)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name = _('Estado')
		verbose_name_plural= _('Estados')


class movimientos(models.Model):
	estado = models.ForeignKey(estados, verbose_name = 'Estado', related_name = 'estado inicial de mov')
	movimiento = models.ForeignKey(estados, verbose_name = 'Movimiento', related_name = 'movimientos')
	descripcion = models.CharField(_('Describe el movimiento'), help_text = 'De que estado'+
		'a que estado se puede mover', max_length = 100, null = True, blank = True)

	def __str__(self):
		return '%s - %s' % (str(self.estado), str(self.movimiento))

	class Meta:
		verbose_name = _('Movimiento')
		verbose_name_plural = _('Movimientos')



