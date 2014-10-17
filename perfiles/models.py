# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from clientes.models import ciudades

# Create your models here.
class perfiles(models.Model):
	user = models.OneToOneField(User,unique=True,related_name='perfil')
	direccion = models.CharField(_('Direccion'),max_length=50)
	ciudad = models.ForeignKey(ciudades, verbose_name = 'Ciudad')
	telefono = models.CharField(_('Telefono'),null=True,blank=True,max_length=20)
	
	def __str__(self):
		return self.user.username
	
	class Meta:
		verbose_name = _('Perfil')
		verbose_name_plural = _('Perfiles')