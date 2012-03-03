from django.db import models

# Create your models here.

class City(models.Model):

	code 		= models.CharField(max_length=3, unique=True)
	name 		= models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.name

class Hotel(models.Model):
	
	city 		= models.ForeignKey(City)
	code 		= models.CharField(max_length=255)
	name 		= models.CharField(max_length=255)

	def __unicode__(self):
		return self.name
