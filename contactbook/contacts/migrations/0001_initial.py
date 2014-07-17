# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'contacts_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('bank', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'contacts', ['Contact'])

        # Adding model 'Company'
        db.create_table(u'contacts_company', (
            (u'contact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contacts.Contact'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('kvk', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('btw', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('branche', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'contacts', ['Company'])

        # Adding model 'Person'
        db.create_table(u'contacts_person', (
            (u'contact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contacts.Contact'], unique=True, primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('works_for', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='employee', null=True, to=orm['contacts.Company'])),
            ('function', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'contacts', ['Person'])

        # Adding unique constraint on 'Person', fields ['first_name', 'last_name']
        db.create_unique(u'contacts_person', ['first_name', 'last_name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Person', fields ['first_name', 'last_name']
        db.delete_unique(u'contacts_person', ['first_name', 'last_name'])

        # Deleting model 'Contact'
        db.delete_table(u'contacts_contact')

        # Deleting model 'Company'
        db.delete_table(u'contacts_company')

        # Deleting model 'Person'
        db.delete_table(u'contacts_person')


    models = {
        u'contacts.company': {
            'Meta': {'object_name': 'Company', '_ormbases': [u'contacts.Contact']},
            'branche': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'btw': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'contact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['contacts.Contact']", 'unique': 'True', 'primary_key': 'True'}),
            'kvk': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bank': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'contacts.person': {
            'Meta': {'unique_together': "(('first_name', 'last_name'),)", 'object_name': 'Person', '_ormbases': [u'contacts.Contact']},
            u'contact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['contacts.Contact']", 'unique': 'True', 'primary_key': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'function': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'works_for': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'employee'", 'null': 'True', 'to': u"orm['contacts.Company']"})
        }
    }

    complete_apps = ['contacts']