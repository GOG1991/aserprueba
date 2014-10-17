# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class estadosCiudades(models.Model):
	"""Clase para controlar las entidades federativas"""
	nombre = models.CharField(max_length = 30, verbose_name = _('Nombre de la entidad federativa'))
	"""Para mostrar el nombre de la entidad en el admin de Django"""
	
	def __str__(self):
		return self.nombre
	
	class Meta:
		verbose_name = _('Entidad federativa')
		verbose_name_plural = _('Entidades federativas')


class ciudades(models.Model):
	"""Clase para controlar las ciudades"""
	estado = models.ForeignKey(estadosCiudades, related_name = 'estados')
	nombre = models.CharField(max_length = 50, verbose_name = _('Nombre de la ciudad'))
	
	def __str__(self):
		return self.nombre
	
	class Meta:
		ordering = ["id"]
		verbose_name = _('Ciudad')
		verbose_name_plural = _('Ciudades')


class reputaciones(models.Model):
	"""Clase para anadir reputaciones a un cliente"""
	nombre = models.CharField(max_length = 50, verbose_name = _('Reputacion'))
	descripcion = models.CharField(max_length = 50, verbose_name = _('Descripcion de la reputacion'), null = True, blank = True)
	color = models.CharField(max_length = 7,default = "#ffffff")
	
	def __str__(self):
		return self.nombre
		#return '%s - %s' % (str(self.nombre), str(self.color))
	
	class Meta:
		verbose_name =_('Reputacion')
		verbose_name_plural= _('Reputaciones')
		#ordering = ['-id']


#constante para definir la ciudad prederterminada
ciudadPredeterminada = 1
class clientes(models.Model):
	"""Clase para controlar el registro de los clientes"""
	nombre = models.CharField(max_length = 100, verbose_name = _('Nombre completo del cliente'))
	telefono1 = models.CharField(max_length = 30, verbose_name = _('Numero telefonico del cliente, campo requerido'))
	direccion = models.CharField(max_length = 50, verbose_name = _('Direccion del cliente, campo requerido'))
	telefono2 = models.CharField(max_length = 30, verbose_name = _('Numero de telefono del cliente'+
		' alternativo'),null = True, blank = True)
	picture = models.ImageField(upload_to = 'images/clientes/', blank = True, null = True, verbose_name='Fotografia del cliente')
	email = models.EmailField(max_length = 75, verbose_name = _('Cuenta de correo electronico'), null = True, blank = True)
	ciudad = models.ForeignKey(ciudades, default=ciudadPredeterminada, related_name = 'ciudades')
	reputacion = models.ManyToManyField(reputaciones, through = 'reputacionesClientes')

	def __str__(self):
		return self.nombre
	
	class Meta:
		verbose_name = _('Cliente')
		verbose_name_plural =_('Clientes')
		ordering = ['nombre']


class personasAutorizadas(models.Model):
	"""Clase para añadir personas autorizadas a un cliente"""
	cliente = models.ForeignKey(clientes, related_name = 'cliente personautorizada')
	nombre = models.CharField(max_length = 100, verbose_name = _('Nombre completo de la persona'))
	telefono = models.CharField(max_length = 30, verbose_name = _('Telefono de contacto'))
	
	def __str__(self):
		return self.nombre
	
	class Meta:
		verbose_name = _('Persona autorizada')
		verbose_name_plural = _('Personas autorizadas')


class reputacionesClientes(models.Model):
	cliente = models.ForeignKey(clientes, related_name = 'cliente')
	reputacion = models.ForeignKey(reputaciones,verbose_name=_('Condición'), related_name = 'reputacion')
	razon = models.CharField(max_length = 100, null = True, blank = True)
	fecha 	= models.DateTimeField(auto_now = True)

	def __str__(self):
		return '%s - %s' % (str(self.cliente), str(self.reputacion))

	class Meta:
		verbose_name = _('Reputacion del cliente')
		verbose_name_plural = _('Reputaciones de los clientes')
		ordering = ['-id']
		