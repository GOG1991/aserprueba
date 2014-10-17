# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm, CharField, Textarea, HiddenInput, Select
from django.forms.widgets import TextInput

from .models import reputaciones, clientes, reputacionesClientes


# forms de esta app.
#con este primer formulario vamos a moficar el atributo del input del formulario de django
class colorAdminForm(ModelForm):
	
	class Meta:
		model = reputaciones
		widgets={'color':TextInput(attrs={'type':'color'}),}


class clienteForm(ModelForm):
	
	class Meta:
		model = clientes
		fields = ('nombre', 'telefono1', 'direccion', 'telefono2', 'email', 'ciudad')

	def __init__(self, *args, **kwargs):
		super(clienteForm, self).__init__(*args, **kwargs)
		self.fields['nombre'].widget.attrs['class'] = 'form-control txtNombre'
		self.fields['nombre'].widget.attrs['id'] = 'txtNombre'
		self.fields['telefono1'].widget.attrs['class'] = 'form-control txtTel'
		self.fields['telefono1'].widget.attrs['id'] = 'txtTel'
		#self.fields['telefono1'].widget.attrs['pattern'] = ''
		self.fields['direccion'].widget.attrs['class'] = 'form-control txtDir'
		self.fields['direccion'].widget.attrs['id'] = 'txtDir'
		#self.fields['picture'].widget.attrs['id'] = 'slctPic'
		#self.fields['picture'].widget.attrs['class'] = 'form-control slctPic'
		self.fields['telefono2'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['ciudad'].widget.attrs['class'] = 'form-control slctCiudad'
		self.fields['ciudad'].widget.attrs['id'] = 'slctCiudad'


class reputacionesForm(ModelForm):

	class Meta:
		model = reputacionesClientes
		fields = ('reputacion', 'razon',)
		widgets = {'reputacion':Select(attrs={'class':'form-control','id':'slctReputacion'}),'razon':forms.HiddenInput(attrs={'class':'form-control','value':'primer condición asignada'}),}


class PictureForm(ModelForm):

	class Meta:
		model = clientes
		fields = ('picture',)

	def __init__(self, *args, **kwargs):
		super(PictureForm, self).__init__(*args, **kwargs)
		self.fields['picture'].widget.attrs['id'] = 'slctPic'
		self.fields['picture'].widget.attrs['class'] = 'form-control slctPic'
		
		

