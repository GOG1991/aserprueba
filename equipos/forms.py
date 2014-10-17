# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm, TextInput , ModelChoiceField ,Select , CharField, SelectMultiple
from django.forms.models import inlineformset_factory

from djangoformsetjs.utils import formset_media_js

from .models import equipos, equipoTieneAccesorios


class equipoForm(forms.ModelForm):

	class Meta:
		model = equipos
		fields = ('marca','categoria','noserie','modelo','descripcion')
		widgets = {
			'marca':Select(attrs={'class':'form-control'}),
			'categoria':Select(attrs={'class':'form-control'}),
			'noserie':TextInput(attrs={'class':'form-control'}),
			'modelo':TextInput(attrs={'class':'form-control','id':'txtModeloE'}),
			'descripcion':forms.Textarea(attrs={'class':'form-control','id':'txtDescE','cols':50,'rows':3}),

		}




class equipoaccesorioForm(forms.ModelForm):

	class Meta:
		model = equipoTieneAccesorios
		exclude = ('equipo',)
		widgets = {
			'accesorio':Select(attrs={'class':'form-control','id':'slctAcce'}),
			'noserie':TextInput(attrs={'class':'form-control'}),
			'descripcion':forms.Textarea(attrs={'class':'form-control','cols':50,'rows':3}),
		}
	class Media(object):
		js = formset_media_js

