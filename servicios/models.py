# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone

from clientes.models import clientes
from perfiles.models import perfiles
from estados.models import estados
from historiales.models import fallas, soluciones
from equipos.models import equipos


class tiposMantenimiento(models.Model):
	nombre = models.CharField(_('Nombre del tipo de mantenimiento'), max_length = 30)
	descripcion = models.TextField(_('Descripción del tipo de mantenimiento'),
		null = True, blank = True)
	
	class Meta:
		verbose_name = _('Tipo de mantenimiento')
		verbose_name_plural = _('Tipos de mantenimiento')
	
	def __str__(self):
		return self.nombre


class tiposServicio(models.Model):
	nombre = models.CharField(_('Nombre del tipo de servicio'), max_length = 30)
	descripcion = models.TextField(_('Descripción del tipo de servicio'),
		null = True, blank = True)	
	
	class Meta:
		verbose_name = _('Tipo de servicio')
		verbose_name_plural = _('Tipos de servicios')
	
	def __str__(self):
		return self.nombre


class productos(models.Model):
	nombre = models.CharField(_('Nombre del producto'), max_length = 50)
	descripcion = models.TextField(_('Descripción del producto'), null = True, blank = True)
	precio = models.DecimalField(max_digits = 10, decimal_places = 2, null = True, blank = True)
	
	class Meta:
		verbose_name = _('Producto')
		verbose_name_plural = _('Productos')
	def __str__(self):
		return self.nombre


class condiciones(models.Model):
	nombre = models.CharField(_('Nombre de la condición'), max_length = 50)
	descripcion = models.TextField(_('Descripción de la condición'), null = True, blank = True)

	class Meta:
		verbose_name = _('Condicion')
		verbose_name_plural = _('Condiciones')
		ordering = ['-id']
	def __str__(self):
		return self.nombre	


class servicios(models.Model):
	cliente = models.ForeignKey(clientes, related_name = 'clientes')
	tipoMant = models.ManyToManyField(tiposMantenimiento, through = 'detalleServicio')
	tipoSer = models.ManyToManyField(tiposServicio, through = 'servicioTieneTipoServicio')
	estado = models.ManyToManyField(estados, through = 'servicioTieneEstados')
	tecnico = models.ManyToManyField(perfiles, through = 'servicioTienePerfil')
	fechaEntrada = models.DateTimeField(editable=False)
	fechaModificacion = models.DateTimeField(auto_now=True)
	fechaTerminado = models.DateTimeField(auto_now = False, null = True, blank = True)
	fechaEntregado = models.DateTimeField(auto_now = False, null = True, blank = True)
	costo = models.DecimalField(max_digits = 6, decimal_places = 2, null = True, blank = True,verbose_name = 'Costo del Servicio',)
	costo_respaldo = models.DecimalField(max_digits = 6, decimal_places = 2, null = True, blank = True,verbose_name = 'Costo de Respaldo',)
	costo_descuento = models.DecimalField(max_digits = 6, decimal_places = 2, null = True, blank = True,verbose_name = 'Descuento %',)
	domicilio = models.CharField(_('Domicilo del servicio'), max_length = 100,
		null = True, blank = True)
	garantia = models.IntegerField(default = 30)
	condicion = models.ForeignKey(condiciones, related_name = 'condiciones', null = True, blank=True, default=1)
	equipo = models.ManyToManyField(equipos, through = 'detalleServicio')
	falla = models.ManyToManyField(fallas, through = 'detalleServicio')
	solucion = models.ManyToManyField(soluciones, through = 'detalleServicio', null=True, blank=True)
	producto = models.ManyToManyField(productos, through = 'servicioTieneProducto', null=True, blank=True)
	
	class Meta:
		verbose_name =_('Servicio')
		verbose_name_plural = _('Servicios')
		ordering = ['-fechaEntrada']
		permissions = ( 
            ( "see_conf", "Ver configuracion del admin" ),
            ( "view_repor", "Ver reportes" ),
        )

	def save(self,*args,**kwargs):
		if not self.id:
			self.fechaEntrada = timezone.now()
		return super(servicios,self).save(*args, **kwargs)
	
	def __str__(self):
		#str para convertir el id del servicio en cadena
		return '%d - %s' % (self.id, str(self.cliente))


class servicioTieneTipoServicio(models.Model):
	"""Clase para controlar el historial de cambio
	de tipo de servicios"""
	servicio = models.ForeignKey(servicios, related_name = 'servicio tipo', verbose_name = 'Servicio',)
	tipo = models.ForeignKey(tiposServicio, related_name = 'tipo servicio', verbose_name = 'Tipo servicio',)
	razonCambio = models.CharField(max_length =100, null = True, blank = True)
	fechaCambio = models.DateTimeField(auto_now = True)
	
	class Meta:
		verbose_name = _('Historial de tipo de servicio')
		verbose_name_plural = _('Historiales de tipo de servicios')
		ordering = ['-id']
	
	def __str__(self):
		return '%s - %s' % (str(self.servicio), str(self.tipo))

	def save(self,*args,**kwargs):
		if not self.id:
			self.fechaCambio = timezone.now()
		return super(servicioTieneTipoServicio,self).save(*args, **kwargs)


class servicioTieneProducto(models.Model):
	servicio = models.ForeignKey(servicios, related_name = 'servicio tiene producto', verbose_name = 'Servicio',)
	producto = models.ForeignKey(productos , related_name = 'productos del servicio', verbose_name = 'Producto',null = True, blank = True)
	cantidad = models.IntegerField(default=1)
	subtotal = models.DecimalField(max_digits = 10, decimal_places = 2, null = True, blank = True, default=0)
	fechaAgregado = models.DateTimeField(editable=False)
	
	class Meta:
		verbose_name = _('Detalle de producto en servicio')
		verbose_name_plural = _('Detalles de productos en servicios')
		ordering = ['-id']
	
	def __str__(self):
		return '%s - %s' % (str(self.servicio), str(self.producto))

	def save(self,*args,**kwargs):
		if not self.id:
			self.fechaAgregado = timezone.now()
		return super(servicioTieneProducto,self).save(*args, **kwargs)


class servicioTienePerfil(models.Model):
	servicio = models.ForeignKey(servicios, related_name = 'servicio perfil', verbose_name = 'Servicio',)
	perfil = models.ForeignKey(perfiles, related_name = 'perfil servicio', verbose_name = 'Tecnico',)
	fechaInicio = models.DateTimeField(_('Fecha inicio'), auto_now = False, null = True, blank = True)
	fechaFin = models.DateTimeField(_('Fecha terminacion'), auto_now = False, null = True, blank = True)
	
	class Meta:
		verbose_name = _('Asiganado al servicio')
		verbose_name_plural = _('Asiganados a los servicios')

	def __str__(self):
		return '%s - %s' % (str(self.servicio), str(self.perfil))

class servicioTieneEstados(models.Model):
	servicio = models.ForeignKey(servicios, verbose_name = 'Servicio', related_name = 'servicio')
	estado = models.ForeignKey(estados, verbose_name = 'Estado', related_name = 'movimiento')
	razonCambio = models.TextField(_('Razon por la que el servicio cambio de estado'))
	fechaCambio = models.DateTimeField(editable=False)
	perfil = models.ForeignKey(User, null=True, blank=True)

	def __str__(self):
		return '%s - %s' % (str(self.servicio), str(self.estado))

	def save(self,*args,**kwargs):
		if not self.id:
			self.fechaCambio = timezone.now()
		return super(servicioTieneEstados,self).save(*args, **kwargs)

	class Meta:
		verbose_name = _('Historial de estados de un servicio')
		verbose_name_plural = _('Historiales de estados de los servicios')
		ordering = ['-id']

sp = 4
class detalleServicio(models.Model):
	servicio = models.ForeignKey(servicios, related_name = 'servicios detalle')
	equipo = models.ForeignKey(equipos, verbose_name = 'Equipo', related_name = 'equipo de servicio')
	falla = models.ForeignKey(fallas, verbose_name = 'Falla del equipo',  related_name = 'fallas')
	mant = models.ForeignKey(tiposMantenimiento, verbose_name = 'Tipo de mantenimiento', default=2)
	solucion = models.ForeignKey(soluciones, default=sp,verbose_name = 'Solución del equipo del se'+
		'rvicio', related_name = 'soluciones', null = True, blank = True)
	revicion = models.BooleanField(_('Revición del equipo del servicio'), )
	password = models.CharField(_('Contraseña para acceder al sistema'), null = True,
		blank=True, max_length=50)
	respaldo = models.CharField(_('Respaldo de la informacion del equipo'), null = True,
		blank=True, max_length=50)
	serviciosSolicitados = models.TextField(_('Servicios solicitados'), )
	observaciones = models.TextField(_('Observaciones del equipo'), help_text = 'Escribe lo más detallado que puedas todo lo que comenta el cliente'
		)

	def __str__(self):
		return '%s - %s' % (str(self.servicio), str(self.equipo))
	class Meta():
		verbose_name = _('Detalle del servicio')
		verbose_name_plural = _('Detalles de los servicios')