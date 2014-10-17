# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.utils.html import format_html, format_html_join
from django.utils.translation import ugettext_lazy as _

from .forms import colorAdminForm
from .models import estadosCiudades, ciudades, clientes, personasAutorizadas, reputaciones,reputacionesClientes


class reputacionesClientesInline(admin.TabularInline):
	model = reputacionesClientes
	verbose_name = _('Reputacion')
	verbose_name_plural = _('Reputaciones')

	def get_extra(self, request, obj = None, **kwargs):
		extra = 1
		if obj:
			return extra
		return extra


class personasAutorizadasInline(admin.TabularInline):
	model = personasAutorizadas
	verbose_name = _('Persona autorizada')
	verbose_name_plural = _('Personas autorizadas')

	def get_extra(self, request, obj = None, **kwargs):
		extra = 1
		if obj:
			return extra
		return extra

class clienteAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','telefono1','direccion')
	list_display_links = ('id', 'nombre')
	search_fields = ('nombre','direccion')
	inlines = [reputacionesClientesInline,personasAutorizadasInline]

class reputacionesAdmin(admin.ModelAdmin):
#el formulario que creamos en forms lo asignamos al form de djangoAdmin
	form = colorAdminForm
	list_display=('nombre','color')
"""	
#class reputacionesClientesAdmin(admin.ModelAdmin):
	#fields = ['cliente', 'fecha']
	#list_display = ('cliente','reputacion_color', 'razon', 'fecha')
	#list_display = ('getCliente',)
#tomar el valor color del modelo reputaciones y mostrarlo en las reputaciones de los clientes
	#def reputacion_color(self,obj):
		#return format_html('<div style="background-color:{0};">{1}</div>',obj.reputacion.color,obj.reputacion.nombre)
		#reputacion_color.allow_tags = True
	#def getCliente(self, obj):
		#return '\n'.join([c.clientes for c in obj.cliente.all()])

#class personasautorizadasAdmin(admin.ModelAdmin):
	#list_display = ('nombre','Cliente')
	#list_filter = ('nombre', 'clientes__nombre')
	#def Cliente(self,obj):
		#return obj.cliente.nombre

#class ciudadesAdmin(admin.ModelAdmin):
	#list_display = ('nombre','estado')

"""
"""
class reputacionesClientesAdmin(admin.ModelAdmin):
	list_display = ('Reputaciones','Clientes', 'Color', 'fecha')
	inlines = [reputacionesClientesInline,]
	exclude = ('cliente',)

	def Reputaciones(self, obj):
		return "\n".join([r.nombre for r in obj.reputacion.all()])

	def Clientes(self, obj):
		return "\n".join([c.nombre for c in obj.cliente.all()])

	def Color(self, obj):
		return format_html('<div style="background-color:{0}; color:{0}";>{0}</div>', format_html_join('\n','{0}',
			((c.color, c.nombre)for c in obj.reputacion.all())))
		Color.allow_tags = True
"""
class ciudadesAdmin(admin.ModelAdmin):
	list_display = ('nombre','estado')

admin.site.register(ciudades,ciudadesAdmin)
admin.site.register(clientes, clienteAdmin)
admin.site.register(reputaciones,reputacionesAdmin)
admin.site.register(estadosCiudades)


"""
class PurchaseOrder(models.Model):
    product = models.ManyToManyField('Product')
    vendor = models.ForeignKey('VendorProfile')
    dollar_amount = models.FloatField(verbose_name='Price')


class Product(models.Model):
   products = models.CharField(max_length=256)

   def __unicode__(self):
       return self.products

admin.py 

class PurchaseOrderAdmin(admin.ModelAdmin):
    fields = ['product', 'dollar_amount']
    list_display = ('get_products', 'vendor')

    def get_products(self, obj):
        return "\n".join([p.products for p in obj.product.all()])

class reputacionesClientesAdmin(admin.Model)
	fields = ['reputacion', 'fecha']
	list_display = ('getReputaciones','razon')

	def getReputaciones(self, obj):
		return "\n".join([r.nombre for r in obj.reputacion.all()])
"""