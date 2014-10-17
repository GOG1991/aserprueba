# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'tiposMantenimiento'
        db.create_table('servicios_tiposmantenimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
        ))
        db.send_create_signal('servicios', ['tiposMantenimiento'])

        # Adding model 'tiposServicio'
        db.create_table('servicios_tiposservicio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
        ))
        db.send_create_signal('servicios', ['tiposServicio'])

        # Adding model 'productos'
        db.create_table('servicios_productos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('precio', self.gf('django.db.models.fields.DecimalField')(max_digits=10, blank=True, decimal_places=2, null=True)),
        ))
        db.send_create_signal('servicios', ['productos'])

        # Adding model 'condiciones'
        db.create_table('servicios_condiciones', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
        ))
        db.send_create_signal('servicios', ['condiciones'])

        # Adding model 'servicios'
        db.create_table('servicios_servicios', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.clientes'], related_name='clientes')),
            ('fechaEntrada', self.gf('django.db.models.fields.DateTimeField')()),
            ('fechaModificacion', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True)),
            ('fechaTerminado', self.gf('django.db.models.fields.DateTimeField')(blank=True, null=True)),
            ('fechaEntregado', self.gf('django.db.models.fields.DateTimeField')(blank=True, null=True)),
            ('costo', self.gf('django.db.models.fields.DecimalField')(max_digits=6, blank=True, decimal_places=2, null=True)),
            ('costo_respaldo', self.gf('django.db.models.fields.DecimalField')(max_digits=6, blank=True, decimal_places=2, null=True)),
            ('domicilio', self.gf('django.db.models.fields.CharField')(blank=True, max_length=100, null=True)),
            ('condicion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['servicios.condiciones'], related_name='condiciones', blank=True, null=True)),
        ))
        db.send_create_signal('servicios', ['servicios'])

        # Adding model 'servicioTieneTipoServicio'
        db.create_table('servicios_serviciotienetiposervicio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('servicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['servicios.servicios'], related_name='servicio tipo')),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['servicios.tiposServicio'], related_name='tipo servicio')),
            ('razonCambio', self.gf('django.db.models.fields.CharField')(blank=True, max_length=100, null=True)),
            ('fechaCambio', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True)),
        ))
        db.send_create_signal('servicios', ['servicioTieneTipoServicio'])

        # Adding model 'servicioTieneProducto'
        db.create_table('servicios_serviciotieneproducto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('servicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['servicios.servicios'], related_name='servicio tiene producto')),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['servicios.productos'], related_name='productos del servicio', blank=True, null=True)),
            ('fechaAgregado', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('servicios', ['servicioTieneProducto'])

        # Adding model 'servicioTienePerfil'
        db.create_table('servicios_serviciotieneperfil', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('servicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['servicios.servicios'], related_name='servicio perfil')),
            ('perfil', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['perfiles.perfiles'], related_name='perfil servicio')),
            ('fechaInicio', self.gf('django.db.models.fields.DateTimeField')(blank=True, null=True)),
            ('fechaFin', self.gf('django.db.models.fields.DateTimeField')(blank=True, null=True)),
        ))
        db.send_create_signal('servicios', ['servicioTienePerfil'])

        # Adding model 'servicioTieneEstados'
        db.create_table('servicios_serviciotieneestados', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('servicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['servicios.servicios'], related_name='servicio')),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['estados.estados'], related_name='movimiento')),
            ('razonCambio', self.gf('django.db.models.fields.TextField')()),
            ('fechaCambio', self.gf('django.db.models.fields.DateTimeField')()),
            ('perfil', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True, null=True)),
        ))
        db.send_create_signal('servicios', ['servicioTieneEstados'])

        # Adding model 'detalleServicio'
        db.create_table('servicios_detalleservicio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('servicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['servicios.servicios'], related_name='servicios detalle')),
            ('equipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['equipos.equipos'], related_name='equipo de servicio')),
            ('falla', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['historiales.fallas'], related_name='fallas')),
            ('mant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['servicios.tiposMantenimiento'])),
            ('solucion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['historiales.soluciones'], related_name='soluciones', default=1, blank=True, null=True)),
            ('revicion', self.gf('django.db.models.fields.BooleanField')()),
            ('password', self.gf('django.db.models.fields.CharField')(blank=True, max_length=50, null=True)),
            ('respaldo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('serviciosSolicitados', self.gf('django.db.models.fields.TextField')()),
            ('observaciones', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('servicios', ['detalleServicio'])


    def backwards(self, orm):
        # Deleting model 'tiposMantenimiento'
        db.delete_table('servicios_tiposmantenimiento')

        # Deleting model 'tiposServicio'
        db.delete_table('servicios_tiposservicio')

        # Deleting model 'productos'
        db.delete_table('servicios_productos')

        # Deleting model 'condiciones'
        db.delete_table('servicios_condiciones')

        # Deleting model 'servicios'
        db.delete_table('servicios_servicios')

        # Deleting model 'servicioTieneTipoServicio'
        db.delete_table('servicios_serviciotienetiposervicio')

        # Deleting model 'servicioTieneProducto'
        db.delete_table('servicios_serviciotieneproducto')

        # Deleting model 'servicioTienePerfil'
        db.delete_table('servicios_serviciotieneperfil')

        # Deleting model 'servicioTieneEstados'
        db.delete_table('servicios_serviciotieneestados')

        # Deleting model 'detalleServicio'
        db.delete_table('servicios_detalleservicio')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'related_name': "'user_set'", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'related_name': "'user_set'", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'clientes.ciudades': {
            'Meta': {'object_name': 'ciudades', 'ordering': "['id']"},
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clientes.estadosCiudades']", 'related_name': "'estados'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'clientes.clientes': {
            'Meta': {'object_name': 'clientes', 'ordering': "['nombre']"},
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clientes.ciudades']", 'related_name': "'ciudades'", 'default': '1'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'reputacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['clientes.reputaciones']", 'symmetrical': 'False', 'through': "orm['clientes.reputacionesClientes']"}),
            'telefono1': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telefono2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'})
        },
        'clientes.estadosciudades': {
            'Meta': {'object_name': 'estadosCiudades'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'clientes.reputaciones': {
            'Meta': {'object_name': 'reputaciones'},
            'color': ('django.db.models.fields.CharField', [], {'default': "'#ffffff'", 'max_length': '7'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'clientes.reputacionesclientes': {
            'Meta': {'object_name': 'reputacionesClientes', 'ordering': "['-id']"},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clientes.clientes']", 'related_name': "'cliente'"}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'razon': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'reputacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clientes.reputaciones']", 'related_name': "'reputacion'"})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'db_table': "'django_content_type'"},
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
            'descripcion': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'equipos.equipos': {
            'Meta': {'object_name': 'equipos'},
            'accesorio': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['equipos.accesorios']", 'symmetrical': 'False', 'through': "orm['equipos.equipoTieneAccesorios']"}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['equipos.categorias']", 'related_name': "'categorias'"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['equipos.marcas']", 'related_name': "'marcas'"}),
            'modelo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'noserie': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'equipos.equipotieneaccesorios': {
            'Meta': {'object_name': 'equipoTieneAccesorios'},
            'accesorio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['equipos.accesorios']", 'related_name': "'accesorios'"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'equipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['equipos.equipos']", 'related_name': "'equipos'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noserie': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'})
        },
        'equipos.marcas': {
            'Meta': {'object_name': 'marcas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'estados.estados': {
            'Meta': {'object_name': 'estados'},
            'descripcion': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'historiales.fallas': {
            'Meta': {'object_name': 'fallas'},
            'categoria': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['equipos.categorias']", 'related_name': "'categoria de falla'", 'symmetrical': 'False'}),
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
            'telefono': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'related_name': "'perfil'", 'unique': 'True'})
        },
        'servicios.condiciones': {
            'Meta': {'object_name': 'condiciones', 'ordering': "['-id']"},
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'servicios.detalleservicio': {
            'Meta': {'object_name': 'detalleServicio'},
            'equipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['equipos.equipos']", 'related_name': "'equipo de servicio'"}),
            'falla': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['historiales.fallas']", 'related_name': "'fallas'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['servicios.tiposMantenimiento']"}),
            'observaciones': ('django.db.models.fields.TextField', [], {}),
            'password': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'respaldo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'revicion': ('django.db.models.fields.BooleanField', [], {}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['servicios.servicios']", 'related_name': "'servicios detalle'"}),
            'serviciosSolicitados': ('django.db.models.fields.TextField', [], {}),
            'solucion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['historiales.soluciones']", 'related_name': "'soluciones'", 'default': '1', 'blank': 'True', 'null': 'True'})
        },
        'servicios.productos': {
            'Meta': {'object_name': 'productos'},
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'blank': 'True', 'decimal_places': '2', 'null': 'True'})
        },
        'servicios.servicios': {
            'Meta': {'object_name': 'servicios', 'ordering': "['-fechaEntrada']"},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clientes.clientes']", 'related_name': "'clientes'"}),
            'condicion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['servicios.condiciones']", 'related_name': "'condiciones'", 'blank': 'True', 'null': 'True'}),
            'costo': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'blank': 'True', 'decimal_places': '2', 'null': 'True'}),
            'costo_respaldo': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'blank': 'True', 'decimal_places': '2', 'null': 'True'}),
            'domicilio': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'equipo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['equipos.equipos']", 'symmetrical': 'False', 'through': "orm['servicios.detalleServicio']"}),
            'estado': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['estados.estados']", 'symmetrical': 'False', 'through': "orm['servicios.servicioTieneEstados']"}),
            'falla': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['historiales.fallas']", 'symmetrical': 'False', 'through': "orm['servicios.detalleServicio']"}),
            'fechaEntrada': ('django.db.models.fields.DateTimeField', [], {}),
            'fechaEntregado': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'fechaModificacion': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'fechaTerminado': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['servicios.productos']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True', 'through': "orm['servicios.servicioTieneProducto']"}),
            'solucion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['historiales.soluciones']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True', 'through': "orm['servicios.detalleServicio']"}),
            'tecnico': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['perfiles.perfiles']", 'symmetrical': 'False', 'through': "orm['servicios.servicioTienePerfil']"}),
            'tipoMant': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['servicios.tiposMantenimiento']", 'symmetrical': 'False', 'through': "orm['servicios.detalleServicio']"}),
            'tipoSer': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['servicios.tiposServicio']", 'symmetrical': 'False', 'through': "orm['servicios.servicioTieneTipoServicio']"})
        },
        'servicios.serviciotieneestados': {
            'Meta': {'object_name': 'servicioTieneEstados', 'ordering': "['-id']"},
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['estados.estados']", 'related_name': "'movimiento'"}),
            'fechaCambio': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perfil': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True'}),
            'razonCambio': ('django.db.models.fields.TextField', [], {}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['servicios.servicios']", 'related_name': "'servicio'"})
        },
        'servicios.serviciotieneperfil': {
            'Meta': {'object_name': 'servicioTienePerfil'},
            'fechaFin': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'fechaInicio': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perfil': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['perfiles.perfiles']", 'related_name': "'perfil servicio'"}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['servicios.servicios']", 'related_name': "'servicio perfil'"})
        },
        'servicios.serviciotieneproducto': {
            'Meta': {'object_name': 'servicioTieneProducto', 'ordering': "['-id']"},
            'fechaAgregado': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['servicios.productos']", 'related_name': "'productos del servicio'", 'blank': 'True', 'null': 'True'}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['servicios.servicios']", 'related_name': "'servicio tiene producto'"})
        },
        'servicios.serviciotienetiposervicio': {
            'Meta': {'object_name': 'servicioTieneTipoServicio', 'ordering': "['-id']"},
            'fechaCambio': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'razonCambio': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['servicios.servicios']", 'related_name': "'servicio tipo'"}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['servicios.tiposServicio']", 'related_name': "'tipo servicio'"})
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