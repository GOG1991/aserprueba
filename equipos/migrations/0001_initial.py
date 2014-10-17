# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'marcas'
        db.create_table('equipos_marcas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('equipos', ['marcas'])

        # Adding model 'categorias'
        db.create_table('equipos_categorias', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('equipos', ['categorias'])

        # Adding model 'accesorios'
        db.create_table('equipos_accesorios', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('equipos', ['accesorios'])

        # Adding model 'equipos'
        db.create_table('equipos_equipos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('marca', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['equipos.marcas'], related_name='marcas')),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['equipos.categorias'], related_name='categorias')),
            ('noserie', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('modelo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('equipos', ['equipos'])

        # Adding model 'equipoTieneAccesorios'
        db.create_table('equipos_equipotieneaccesorios', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('equipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['equipos.equipos'], related_name='equipos')),
            ('accesorio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['equipos.accesorios'], related_name='accesorios')),
            ('noserie', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('equipos', ['equipoTieneAccesorios'])


    def backwards(self, orm):
        # Deleting model 'marcas'
        db.delete_table('equipos_marcas')

        # Deleting model 'categorias'
        db.delete_table('equipos_categorias')

        # Deleting model 'accesorios'
        db.delete_table('equipos_accesorios')

        # Deleting model 'equipos'
        db.delete_table('equipos_equipos')

        # Deleting model 'equipoTieneAccesorios'
        db.delete_table('equipos_equipotieneaccesorios')


    models = {
        'equipos.accesorios': {
            'Meta': {'object_name': 'accesorios'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'equipos.categorias': {
            'Meta': {'object_name': 'categorias'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'equipos.equipos': {
            'Meta': {'object_name': 'equipos'},
            'accesorio': ('django.db.models.fields.related.ManyToManyField', [], {'through': "orm['equipos.equipoTieneAccesorios']", 'to': "orm['equipos.accesorios']", 'symmetrical': 'False'}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['equipos.categorias']", 'related_name': "'categorias'"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['equipos.marcas']", 'related_name': "'marcas'"}),
            'modelo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'noserie': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'equipos.equipotieneaccesorios': {
            'Meta': {'object_name': 'equipoTieneAccesorios'},
            'accesorio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['equipos.accesorios']", 'related_name': "'accesorios'"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'equipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['equipos.equipos']", 'related_name': "'equipos'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noserie': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'equipos.marcas': {
            'Meta': {'object_name': 'marcas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['equipos']