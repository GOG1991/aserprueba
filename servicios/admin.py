# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import tiposMantenimiento, tiposServicio, productos, servicios, servicioTieneTipoServicio, servicioTieneProducto, servicioTienePerfil, servicioTieneEstados, detalleServicio, condiciones

"""
class servicioTieneTipoMantInline(admin.TabularInline):
	model = servicioTieneTipoMant
	extra = 1
	verbose_name = _('Tipo mantenimiento')
	verbose_name_plural = _('Tipos mantenimientos')
"""

class servicioTieneTipoServicioInline(admin.TabularInline):
	model = servicioTieneTipoServicio
	extra = 1
	verbose_name = _('Tipo servicio')
	verbose_name_plural = _('Tipos servicios')
	

class servicioTieneEstadosInline(admin.TabularInline):
	model = servicioTieneEstados
	extra = 1
	verbose_name = _('Estado')
	verbose_name_plural = _('Estados')

class servicioTieneEstadosAdmin(admin.ModelAdmin):
	
	def save_model(self,request,obj,form,change):
			obj.pefil = request.user
			obj.save()


class servicioTieneProductoInline(admin.TabularInline):
	model = servicioTieneProducto
	extra = 1
	verbose_name = _('Producto')
	verbose_name_plural = _('Productos')
	raw_id_fields = ('producto',)


class detalleServicioInline(admin.StackedInline):
	model = detalleServicio
	extra = 1
	verbose_name = _('Equipo')
	verbose_name_plural = _('Equipos')
	raw_id_fields = ('equipo',)


class servicioTienePerfilInline(admin.StackedInline):
	model = servicioTienePerfil
	extra = 1
	verbose_name = _('Tecnico')
	verbose_name_plural = _('Tecnicos')
	

class servicioAdmin(admin.ModelAdmin):
	list_display = ('id', 'cliente',)
	raw_id_fields = ('cliente',)
	inlines = [servicioTieneTipoServicioInline, servicioTieneEstadosInline, servicioTieneProductoInline, detalleServicioInline, servicioTienePerfilInline]


admin.site.register(servicios,servicioAdmin)
admin.site.register(productos)
admin.site.register(tiposServicio)
admin.site.register(tiposMantenimiento)
admin.site.register(condiciones)
admin.site.register(servicioTieneEstados)