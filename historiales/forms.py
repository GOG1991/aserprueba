# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm, TextInput , ModelChoiceField ,Select , CharField, SelectMultiple

from .models import fallas, soluciones

class fallaForm(forms.ModelForm):

	class Meta:
		model = fallas

		widgets = {
			'nombre':TextInput(attrs={'class':'form-control txtFalla','id':'txtnameF'}),
			'descripcion':forms.Textarea(attrs={'class':'form-control txtDescF','cols':50,'rows':3,'id':'txtDescF'}),
			'categoria':forms.SelectMultiple(attrs={'class':'form-control','id':'slctCatF'}),
		}

class solucionForm(forms.ModelForm):

	class Meta:
		model = soluciones
		widgets = {
			'nombre':TextInput(attrs={'class':'form-control','id':'txtSol'}),
			'descripcion':forms.Textarea(attrs={'class':'form-control','cols':50,'rows':3}),
		}
		