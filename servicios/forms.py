# -*- encoding: utf-8 -*-
from django import forms 
from django.forms import ModelForm, TextInput , ModelChoiceField ,Select , CharField, SelectMultiple ,NumberInput

from djangoformsetjs.utils import formset_media_js

from .models import servicios, servicioTieneEstados, detalleServicio, servicioTieneTipoServicio, servicioTieneProducto, servicioTienePerfil,productos


class costoForm(ModelForm):

	class Meta:
		model = servicios
		fields = ('costo','costo_respaldo','costo_descuento')
		widgets = {
			'costo':TextInput(attrs={'class':'form-control','id':'txtCostoS' ,'placeholder':'Escribe el costo de la mano de obra','value':'0'}),
			'costo_respaldo':TextInput(attrs={'class':'form-control','id':'txtCostoR','placeholder':'Escribe el costo de respaldo','value':'0'}),
			'costo_descuento':TextInput(attrs={'class':'form-control','id':'txtDesc','placeholder':'Descuento al servicio en porcentaje','value':'0'})
		}

class registroServicio(ModelForm):
	
	class Meta:
		model = servicios 
		
		fields = ('cliente','domicilio','tipoMant','tipoSer','estado')
		widgets = {
			'cliente':  Select(attrs={'class': 'form-control', 'id':'txtCliente', 'name':'txtCliente'}),
			'domicilio': TextInput(attrs={'class': 'form-control', 'id':'txtDireccion', 'name':'txtDireccion','disabled':'disabled'}),
			'tipoMant' : Select(attrs={'class':'form-control','id':'slctTipoMant'}),
			'tipoSer' : Select(attrs={'class':'form-control','id':'slctTipoServ'}),
			'estado' : Select(attrs={'class':'form-control','id':'slctEstado'}),
		}


class servicioForm(ModelForm):
	
	class Meta:
		model = servicios
		fields = ('condicion','cliente','domicilio',)
		widgets = {
			'cliente':forms.HiddenInput(attrs={'placeholder':'clic aquí para buscar al cliente','class':'form-control','id':'txtCliente'}),'domicilio':TextInput(attrs={'class':'form-control','id':'txtDireccion','disabled':'disabled'}),
			 'condicion':Select(attrs={'class':'form-control'}),
			 }


class detalleServicioForm(ModelForm):

	class Meta:
		model = detalleServicio
		exclude =('solucion',)

		widgets = {'equipo':TextInput(attrs={'placeholder':'clic aqui para añadir un equipo','class':'form-control txtSelEquipo','id':'slctEquipo','name':'txtSelEquipo'}),'password':TextInput(
					attrs={'class':'form-control txtContraseña','id':'txtContraseña','placeholder':'contraseña del equipo'}),'respaldo':forms.TextInput(attrs={'class':'form-control txtRes','list':'listrepaldos'}),#'disabled':'disabled'
					'falla':TextInput(attrs={'placeholder':'clic aquí para agregar falla','class':'form-control txtFalla','id':'txtFalla'}),'revicion':forms.CheckboxInput(attrs={'class':'chkRev'}),'serviciosSolicitados':
							TextInput(attrs={'class':'form-control','list':'solicitudesCli'}),'observaciones':forms.Textarea(attrs={'class':'form-control','cols':50,'rows':3}),'mant':Select(attrs={'class':'form-control','id':'slctTipoMant'}),}
	class Media(object):
		js = formset_media_js


class solucionForm(ModelForm):

	class Meta:
		model = detalleServicio
		fields = ('solucion','equipo')
		widgets = {'solucion':Select(attrs = {'class':'form-control slctSol'}),
				   'equipo':Select(attrs = {'class':'form-control'}),}



class servicioTieneEstadosForm(ModelForm):

	class Meta:
		model = servicioTieneEstados
		exclude = ('perfil','razonCambio',)
		widgets = {'estado':forms.HiddenInput(attrs={'class':'form-control','id':'slctEstado','value':'1'}),'perfil':Select(attrs={'class':'form-control'}),}

"""
class servicioTieneTipoMantForm(ModelForm):

	class Meta:
		model = servicioTieneTipoMant
		fields = ('tipoMant',)
		widgets = {'tipoMant':Select(attrs={'class':'form-control','id':'slctTipoMant'}),}
"""

class cambioEstadoForm(ModelForm):

	class Meta:
		model = servicioTieneEstados
		fields = ('razonCambio',)
		widgets = {'razonCambio':TextInput(attrs={'class':'form-control','id':'txtRazon','value':'sin descripción'}),
				   'estado':Select(attrs={'class':'form-control'}),
		}


class cambioEdoFin(ModelForm):
	
	class Meta:
		model = servicioTieneEstados
		fields = ('estado','razonCambio',)
		widgets = {'estado':forms.HiddenInput(attrs={'class':'form-control','id':'txtEdo','value':'5',}),
				   'razonCambio':forms.HiddenInput(attrs={'class':'form-control','value':'equipos entregados al cliente',}),
		}

class cambioGarantia(ModelForm):

	class Meta:
		model = servicios
		fields = ('garantia',)
		widgets = {'garantia':forms.NumberInput(attrs={'class':'form-control'})
		}		


class servicioTieneTipoServicioForm(ModelForm):

	class Meta:
		model = servicioTieneTipoServicio
		fields = ('tipo',)
		widgets = {'tipo':Select(attrs={'class':'form-control','id':'slctTipoSer'}),}


class servicioProductoForm(ModelForm):

	class Meta:
		model = servicioTieneProducto
		fields = ('producto','cantidad')
		widgets = { 'producto':Select(attrs={'class':'form-control','id':'slctProducto'}),
					'cantidad':forms.NumberInput(attrs={'class':'form-control','type':'number','min':'1'}),
		}


class servicioTecnicoForm(ModelForm):

	class Meta:
		model = servicioTienePerfil
		fields = ('perfil','fechaInicio','fechaFin')
		widgets = { 'perfil':Select(attrs={'class':'form-control','id':'slctTecnico'}),'fechaInicio':forms.DateInput(format='%Y-%m-%d %H:%M:%S',attrs={'class':'form-control','id':'fechaInicio',
				'disabled':'disabled'}),'fechaFin':forms.DateInput(format='%Y-%m-%d %H:%M:%S',attrs={'class':'form-control','id':'fechaFin','disabled':'disabled'}), }

class servicioProd(ModelForm):

	class Meta:
		model = servicios
		fields = ('cliente',)


class domicilioForm(forms.Form):
	domicilio = forms.CharField(max_length=50)


class productosForm(ModelForm):
	class Meta:
		model = productos
		widgets = {'nombre':TextInput(attrs ={'class':'form-control','placeholder':'escribe el nombre del producto' }),
				   'descripcion':forms.Textarea(attrs={'class':'form-control','id':'txtRazon','cols':50,'rows':3,'placeholder':'Describe detalladamente el producto'}),
				   'precio':NumberInput(attrs={'class':'form-control','min':'0'}),
				   }


