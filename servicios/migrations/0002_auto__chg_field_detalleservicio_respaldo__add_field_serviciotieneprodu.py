# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'detalleServicio.respaldo'
        db.alter_column('servicios_detalleservicio', 'respaldo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))
        # Adding field 'servicioTieneProducto.cantidad'
        db.add_column('servicios_serviciotieneproducto', 'cantidad',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'detalleServicio.respaldo'
        db.alter_column('servicios_detalleservicio', 'respaldo', self.gf('django.db.models.fields.BooleanField')())
        # Deleting field 'servicioTieneProducto.cantidad'
        db.delete_column('servicios_serviciotieneproducto', 'cantidad')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'clientes.ciudades': {
            'Meta': {'object_name': 'ciudades', 'ordering': "['id']"},
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'estados'", 'to': "orm['clientes.estadosCiudades']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'clientes.clientes': {
            'Meta': {'object_name': 'clientes', 'ordering': "['nombre']"},
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'ciudades'", 'to': "orm['clientes.ciudades']"}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.EmailField', [], {'null': 'True', 'blank': 'True', 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'reputacion': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['clientes.reputaciones']", 'through': "orm['clientes.reputacionesClientes']"}),
            'telefono1': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefono2': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'})
        },
        'clientes.estadosciudades': {
            'Meta': {'object_name': 'estadosCiudades'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
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
            'fecha': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'razon': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'reputacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reputacion'", 'to': "orm['clientes.reputaciones']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'equipos.accesorios': {
            'Meta': {'object_name': 'accesorios'},
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'equipos.categorias': {
            'Meta': {'object_name': 'categorias'},
            'descripcion': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'equipos.equipos': {
            'Meta': {'object_name': 'equipos'},
            'accesorio': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['equipos.accesorios']", 'through': "orm['equipos.equipoTieneAccesorios']"}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'categorias'", 'to': "orm['equipos.categorias']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'marcas'", 'to': "orm['equipos.marcas']"}),
            'modelo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'noserie': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'equipos.equipotieneaccesorios': {
            'Meta': {'object_name': 'equipoTieneAccesorios'},
            'accesorio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'accesorios'", 'to': "orm['equipos.accesorios']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'equipo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equipos'", 'to': "orm['equipos.equipos']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noserie': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'})
        },
        'equipos.marcas': {
            'Meta': {'object_name': 'marcas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'estados.estados': {
            'Meta': {'object_name': 'estados'},
            'descripcion': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'historiales.fallas': {
            'Meta': {'object_name': 'fallas'},
            'categoria': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'categoria de falla'", 'to': "orm['equipos.categorias']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'historiales.soluciones': {
            'Meta': {'object_name': 'soluciones'},
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'perfiles.perfiles': {
            'Meta': {'object_name': 'perfiles'},
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clientes.ciudades']"}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '20'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'related_name': "'perfil'", 'to': "orm['auth.User']"})
        },
        'servicios.condiciones': {
            'Meta': {'object_name': 'condiciones', 'ordering': "['-id']"},
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'servicios.detalleservicio': {
            'Meta': {'object_name': 'detalleServicio'},
            'equipo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equipo de servicio'", 'to': "orm['equipos.equipos']"}),
            'falla': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fallas'", 'to': "orm['historiales.fallas']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['servicios.tiposMantenimiento']"}),
            'observaciones': ('django.db.models.fields.TextField', [], {}),
            'password': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'respaldo': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True'}),
            'revicion': ('django.db.models.fields.BooleanField', [], {}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'servicios detalle'", 'to': "orm['servicios.servicios']"}),
            'serviciosSolicitados': ('django.db.models.fields.TextField', [], {}),
            'solucion': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'soluciones'", 'null': 'True', 'to': "orm['historiales.soluciones']", 'blank': 'True'})
        },
        'servicios.productos': {
            'Meta': {'object_name': 'productos'},
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'blank': 'True', 'null': 'True', 'max_digits': '10'})
        },
        'servicios.servicios': {
            'Meta': {'object_name': 'servicios', 'ordering': "['-fechaEntrada']"},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'clientes'", 'to': "orm['clientes.clientes']"}),
            'condicion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'condiciones'", 'null': 'True', 'to': "orm['servicios.condiciones']", 'blank': 'True'}),
            'costo': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'blank': 'True', 'null': 'True', 'max_digits': '6'}),
            'costo_respaldo': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'blank': 'True', 'null': 'True', 'max_digits': '6'}),
            'domicilio': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'equipo': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['equipos.equipos']", 'through': "orm['servicios.detalleServicio']"}),
            'estado': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['estados.estados']", 'through': "orm['servicios.servicioTieneEstados']"}),
            'falla': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['historiales.fallas']", 'through': "orm['servicios.detalleServicio']"}),
            'fechaEntrada': ('django.db.models.fields.DateTimeField', [], {}),
            'fechaEntregado': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'fechaModificacion': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'fechaTerminado': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['servicios.productos']", 'null': 'True', 'blank': 'True', 'through': "orm['servicios.servicioTieneProducto']"}),
            'solucion': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['historiales.soluciones']", 'null': 'True', 'blank': 'True', 'through': "orm['servicios.detalleServicio']"}),
            'tecnico': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['perfiles.perfiles']", 'through': "orm['servicios.servicioTienePerfil']"}),
            'tipoMant': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['servicios.tiposMantenimiento']", 'through': "orm['servicios.detalleServicio']"}),
            'tipoSer': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['servicios.tiposServicio']", 'through': "orm['servicios.servicioTieneTipoServicio']"})
        },
        'servicios.serviciotieneestados': {
            'Meta': {'object_name': 'servicioTieneEstados', 'ordering': "['-id']"},
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'movimiento'", 'to': "orm['estados.estados']"}),
            'fechaCambio': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perfil': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'razonCambio': ('django.db.models.fields.TextField', [], {}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'servicio'", 'to': "orm['servicios.servicios']"})
        },
        'servicios.serviciotieneperfil': {
            'Meta': {'object_name': 'servicioTienePerfil'},
            'fechaFin': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'fechaInicio': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perfil': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'perfil servicio'", 'to': "orm['perfiles.perfiles']"}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'servicio perfil'", 'to': "orm['servicios.servicios']"})
        },
        'servicios.serviciotieneproducto': {
            'Meta': {'object_name': 'servicioTieneProducto', 'ordering': "['-id']"},
            'cantidad': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fechaAgregado': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'productos del servicio'", 'null': 'True', 'to': "orm['servicios.productos']", 'blank': 'True'}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'servicio tiene producto'", 'to': "orm['servicios.servicios']"})
        },
        'servicios.serviciotienetiposervicio': {
            'Meta': {'object_name': 'servicioTieneTipoServicio', 'ordering': "['-id']"},
            'fechaCambio': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'razonCambio': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'servicio tipo'", 'to': "orm['servicios.servicios']"}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tipo servicio'", 'to': "orm['servicios.tiposServicio']"})
        },
        'servicios.tiposmantenimiento': {
            'Meta': {'object_name': 'tiposMantenimiento'},
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'servicios.tiposservicio': {
            'Meta': {'object_name': 'tiposServicio'},
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['servicios']