# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Hotel.hotelcode'
        db.delete_column('hotels_hotel', 'hotelcode')

        # Adding field 'Hotel.code'
        db.add_column('hotels_hotel', 'code', self.gf('django.db.models.fields.CharField')(default='doei', max_length=255), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Hotel.hotelcode'
        db.add_column('hotels_hotel', 'hotelcode', self.gf('django.db.models.fields.CharField')(default='hallo', max_length=255), keep_default=False)

        # Deleting field 'Hotel.code'
        db.delete_column('hotels_hotel', 'code')


    models = {
        'hotels.city': {
            'Meta': {'object_name': 'City'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'hotels.hotel': {
            'Meta': {'object_name': 'Hotel'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hotels.City']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['hotels']
