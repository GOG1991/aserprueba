# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm, TextInput , ModelChoiceField ,Select , CharField, SelectMultiple

from .models import estados, movimientos

# forms de esta app.
class movimientoForm(ModelForm):

	class Meta:
		model = movimientos
		estado = forms.ModelChoiceField(queryset = estados.objects.all())
		movimiento = forms.ModelChoiceField(queryset=estados.objects.all())

		widgets = {'estado':Select(attrs={'class':'form-control'}),}

