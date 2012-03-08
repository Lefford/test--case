"""	
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test import TestCase
from utils import get_remote_content
from hotels.models import City, Hotel
from django.test.client import Client
from hotels.management.commands.importcity import save_city
from hotels.management.commands.importhotel import save_hotel

class MaykinTestCase(TestCase):
	fixtures = ['hotels.json']

	def setUp(self):
		self.url = 'http://python-demo.maykin.nl/'
		self.username = 'python-demo'
		self.password = 'claw30_bumps'
		self.city_csv_uri = 'city.csv'
		self.hotel_csv_uri = 'hotel.csv'
		self.c = Client()

	def import_city_data(self):
		""" 
		Test: get city.csv remotley
		"""

		file_uri = 'city.csv'
		remote_data = get_remote_content(self.url+file_uri, self.username, self.password)
		self.assertEqual(remote_data['response_code'], 200)

	def import_hotel_data(self):
		"""
		Test: get hotel.csv remotely
		"""

		file_uri = 'hotel.csv'
		remote_data = get_remote_content(self.url+file_uri, self.username, self.password)
		self.assertEqual(remote_data['response_code'], 200)

	def store_city(self):
		"""
		Store cities from csv in base
		"""

		file_uri = self.city_csv_uri
		data = get_remote_content(self.url+file_uri, self.username, self.password)
		csv_city = data['data']

		save_city(csv_city)
		total_new_cities = City.objects.all().count()
		
		self.assertEqual(total_new_cities, 6)
		
	def store_hotel(self):
		"""
		Store hotel from csv in base	
		"""
		
		# first get the cities 
		self.store_city()

		file_uri = self.hotel_csv_uri
		data = get_remote_content(self.url+file_uri, self.username, self.password)

		hotel_csv = data['data']
		save_hotel(hotel_csv)
		total_new_hotels = Hotel.objects.all().count()

		self.assertEqual(total_new_hotels, 196)
		
	def get_hotels_view(self):
		"""
		Useless test, wish i could get the json data en validate the out 
		"""	
		response = self.c.get('/test-form/', {'city': 'ANT'},
				 HTTP_X_REQUEST_WITH='XMLHttpRequest')
		
		self.assertEqual(respons.status_code, 200)

	def submit_city_hotel_view(self):
		"""
		after a successful post redirect to decision-page
		"""
		response = self.c.post('/test-form/', {'cities': 'BAR', 'hotels': 'BAR09'}, follow=True)

		self.assertEqual(response.redirect_chain[0][1], 302)
