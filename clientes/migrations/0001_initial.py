# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'estadosCiudades'
        db.create_table('clientes_estadosciudades', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('clientes', ['estadosCiudades'])

        # Adding model 'ciudades'
        db.create_table('clientes_ciudades', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(related_name='estados', to=orm['clientes.estadosCiudades'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('clientes', ['ciudades'])

        # Adding model 'reputaciones'
        db.create_table('clientes_reputaciones', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=50)),
            ('color', self.gf('django.db.models.fields.CharField')(default='#ffffff', max_length=7)),
        ))
        db.send_create_signal('clientes', ['reputaciones'])

        # Adding model 'clientes'
        db.create_table('clientes_clientes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('telefono1', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('telefono2', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=30)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(null=True, blank=True, max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(null=True, blank=True, max_length=75)),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ciudades', to=orm['clientes.ciudades'], default=1)),
        ))
        db.send_create_signal('clientes', ['clientes'])

        # Adding model 'personasAutorizadas'
        db.create_table('clientes_personasautorizadas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cliente personautorizada', to=orm['clientes.clientes'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('clientes', ['personasAutorizadas'])

        # Adding model 'reputacionesClientes'
        db.create_table('clientes_reputacionesclientes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cliente', to=orm['clientes.clientes'])),
            ('reputacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reputacion', to=orm['clientes.reputaciones'])),
            ('razon', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=100)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('clientes', ['reputacionesClientes'])


    def backwards(self, orm):
        # Deleting model 'estadosCiudades'
        db.delete_table('clientes_estadosciudades')

        # Deleting model 'ciudades'
        db.delete_table('clientes_ciudades')

        # Deleting model 'reputaciones'
        db.delete_table('clientes_reputaciones')

        # Deleting model 'clientes'
        db.delete_table('clientes_clientes')

        # Deleting model 'personasAutorizadas'
        db.delete_table('clientes_personasautorizadas')

        # Deleting model 'reputacionesClientes'
        db.delete_table('clientes_reputacionesclientes')


    models = {
        'clientes.ciudades': {
            'Meta': {'object_name': 'ciudades', 'ordering': "['id']"},
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'estados'", 'to': "orm['clientes.estadosCiudades']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'clientes.clientes': {
            'Meta': {'object_name': 'clientes', 'ordering': "['nombre']"},
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ciudades'", 'to': "orm['clientes.ciudades']", 'default': '1'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.EmailField', [], {'null': 'True', 'blank': 'True', 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'reputacion': ('django.db.models.fields.related.ManyToManyField', [], {'through': "orm['clientes.reputacionesClientes']", 'to': "orm['clientes.reputaciones']", 'symmetrical': 'False'}),
            'telefono1': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefono2': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'})
        },
        'clientes.estadosciudades': {
            'Meta': {'object_name': 'estadosCiudades'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'clientes.personasautorizadas': {
            'Meta': {'object_name': 'personasAutorizadas'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cliente personautorizada'", 'to': "orm['clientes.clientes']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'clientes.reputaciones': {
            'Meta': {'object_name': 'reputaciones'},
            'color': ('django.db.models.fields.CharField', [], {'default': "'#ffffff'", 'max_length': '7'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'clientes.reputacionesclientes': {
            'Meta': {'object_name': 'reputacionesClientes', 'ordering': "['-id']"},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cliente'", 'to': "orm['clientes.clientes']"}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'razon': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'reputacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reputacion'", 'to': "orm['clientes.reputaciones']"})
        }
    }

    complete_apps = ['clientes']