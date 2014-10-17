# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class marcas(models.Model):
	nombre = models.CharField(_('Nombre de la marca'), max_length = 30)

	class Meta:
		verbose_name = _('Marca')
		verbose_name_plural = _('Marcas')
	def __str__(self):
		return self.nombre


class categorias(models.Model):
	nombre = models.CharField(_('Nombre de la categoria'),max_length = 30)
	descripcion = models.CharField(_('Descripcion '+
		'de la categoria'),max_length = 50, null = True, blank = True)

	class Meta:
		verbose_name =_ ('Categoria')
		verbose_name_plural = _('Categorias')

	def __str__(self):
		return self.nombre


class accesorios(models.Model):
	nombre = models.CharField(_('Nombre generico del accesorio'),max_length = 40)
	descripcion = models.TextField(_('Descripcion'+
		' general del accesorio'), null=True, blank=True)
	
	class Meta:
		verbose_name = _('Accesorios')
		verbose_name_plural = _('Accesorios')
	
	def __str__(self):
		return self.nombre


class equipos(models.Model):
	marca = models.ForeignKey(marcas, related_name = 'marcas')
	categoria = models.ForeignKey(categorias, related_name = 'categorias')
	noserie = models.CharField(_('Número de serie del equipo'), max_length = 50)
	modelo = models.CharField(_('Modelo del equipo'), max_length = 50)
	descripcion = models.TextField(_('Descripcion del equipo'),null = True,
		blank = True, help_text = 'Describe el equipo la primera vez que ingresa'+
		' a la empresa')
	accesorio = models.ManyToManyField(accesorios, through = 'equipoTieneAccesorios')
	
	class Meta:
		verbose_name = _('Equipo')
		verbose_name_plural = _('Equipos')
	
	def __str__(self):
		return '%s %s %s' % (self.marca, self.modelo, self.noserie)


class equipoTieneAccesorios(models.Model):
	equipo = models.ForeignKey(equipos, related_name = 'equipos')
	accesorio = models.ForeignKey(accesorios, related_name = 'accesorios', default=1)
	noserie = models.CharField(_('Número de serie del accesorio del equipo'), max_length=50, null=True, blank=True)
	descripcion = models.TextField(_('Descripcion'+
		' del accesorio del equipo'), null = True, blank = True)
	
	class Meta:
		verbose_name = _('Accesorio del equipo')
		verbose_name_plural =_('Accesorios de los equipos')
	
	def __str__(self):
		return '%s - %s - %s' % (str(self.equipo),str(self.accesorio), self.noserie)

		