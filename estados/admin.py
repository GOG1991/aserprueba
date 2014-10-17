# -*- encoding: utf-8 -*-
from django.contrib import admin

from .models import estados, movimientos
from .forms import movimientoForm
# Register your models here.

#class moviminetosAdmin(admin.ModelAdmin):
	#form = movimientoForm
	#list_display = ('estado','movimiento','descripcion')

#class estadosAdmin(admin.ModelAdmin):
	#list_display = ('nombre', 'descripcion')

admin.site.register(estados)#,estadosAdmin)
admin.site.register(movimientos)#,moviminetosAdmin)