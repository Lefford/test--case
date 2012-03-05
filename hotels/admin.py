from hotels.models import City, Hotel
from django.contrib import admin
from django import forms

class HotelAdmin(admin.ModelAdmin):
	list_display =['name', 'code']

class CityAdmin(admin.ModelAdmin):
	list_display=['name', 'code']

admin.site.register(City, HotelAdmin)
admin.site.register(Hotel, CityAdmin)
