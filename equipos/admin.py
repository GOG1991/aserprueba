# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import marcas, categorias, equipos, accesorios, equipoTieneAccesorios

#class accesoriosAdmin(admin.ModelAdmin):
	#list_display = ('nombre','descripcion')

#class categoriasAdmin(admin.ModelAdmin):
	#list_display = ('nombre', 'descripcion')

#class equiposAdmin(admin.ModelAdmin):
	#list_display = ('noserie', 'modelo', 'marca', 'categoria')
	#search_fields = ('noserie','modelo')
	#list_filter = ('marca', 'categoria')

class equipoTieneAccesoriosInline(admin.TabularInline):
	model = equipoTieneAccesorios
	extra = 0


class equipoAdmin(admin.ModelAdmin):
	list_display = ('noserie', 'modelo', 'marca','categoria')
	search_fields = ('noserie','modelo')
	list_filter = ('marca', 'categoria')
	inlines = [equipoTieneAccesoriosInline,]


class equipoAccesorioAdmin(admin.ModelAdmin):
	list_display = ('accesorio', 'noserie', 'equipo')
	search_fields = ('noserie', 'equipo',)
	list_filter = ('accesorio', 'equipo')
	raw_id_fields = ('equipo',)

admin.site.register(marcas)
admin.site.register(categorias)#,categoriasAdmin)
admin.site.register(equipos, equipoAdmin)#,equiposAdmin)
admin.site.register(accesorios)#, accesoriosAdmin)