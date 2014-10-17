# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'fallas'
        db.create_table('historiales_fallas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
        ))
        db.send_create_signal('historiales', ['fallas'])

        # Adding M2M table for field categoria on 'fallas'
        m2m_table_name = db.shorten_name('historiales_fallas_categoria')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('fallas', models.ForeignKey(orm['historiales.fallas'], null=False)),
            ('categorias', models.ForeignKey(orm['equipos.categorias'], null=False))
        ))
        db.create_unique(m2m_table_name, ['fallas_id', 'categorias_id'])

        # Adding model 'soluciones'
        db.create_table('historiales_soluciones', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
        ))
        db.send_create_signal('historiales', ['soluciones'])


    def backwards(self, orm):
        # Deleting model 'fallas'
        db.delete_table('historiales_fallas')

        # Removing M2M table for field categoria on 'fallas'
        db.delete_table(db.shorten_name('historiales_fallas_categoria'))

        # Deleting model 'soluciones'
        db.delete_table('historiales_soluciones')


    models = {
        'equipos.categorias': {
            'Meta': {'object_name': 'categorias'},
            'descripcion': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'historiales.fallas': {
            'Meta': {'object_name': 'fallas'},
            'categoria': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'categoria de falla'", 'to': "orm['equipos.categorias']", 'symmetrical': 'False'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'historiales.soluciones': {
            'Meta': {'object_name': 'soluciones'},
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['historiales']