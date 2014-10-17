# -*- encoding: utf-8 -*-
from django import forms


class loginForm(forms.Form):
	username = forms.CharField(
		label = 'Nombre de usuario',
		widget = forms.TextInput(
			attrs = {
			'class':'form-control',
			'placeholder':'Nombre de usuario',
		}))
	password = forms.CharField(
		label='Password',
		widget = forms.PasswordInput(
			render_value = False,
			attrs = {
			'class':'form-control',
			'placeholder':'Password',
		}))