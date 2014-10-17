# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'estados'
        db.create_table('estados_estados', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=100)),
        ))
        db.send_create_signal('estados', ['estados'])

        # Adding model 'movimientos'
        db.create_table('estados_movimientos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estados.estados'], related_name='estado inicial de mov')),
            ('movimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estados.estados'], related_name='movimientos')),
            ('descripcion', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=100)),
        ))
        db.send_create_signal('estados', ['movimientos'])


    def backwards(self, orm):
        # Deleting model 'estados'
        db.delete_table('estados_estados')

        # Deleting model 'movimientos'
        db.delete_table('estados_movimientos')


    models = {
        'estados.estados': {
            'Meta': {'object_name': 'estados'},
            'descripcion': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'estados.movimientos': {
            'Meta': {'object_name': 'movimientos'},
            'descripcion': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estados.estados']", 'related_name': "'estado inicial de mov'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estados.estados']", 'related_name': "'movimientos'"})
        }
    }

    complete_apps = ['estados']