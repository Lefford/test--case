from celery.decorators import periodic_task
from celery.task.schedules import crontab
from hotels.management.commands.importcity import save_city
from hotels.management.commands.importhotel import save_hotel
from utils import get_remote_content

URL= 'http://python-demo.maykin.nl/'
USERNAME= 'python-demo'
PASSWORD='claw30_bumps' 

@periodic_task(run_every=crontab())
def import_city():
"""
runs city import every minute 
"""
	city_uri = 'city.csv'  

	data = get_remote_content(URL+city_uri, USERNAME, PASSWORD)
	save_city(data)

	
@periodic_task(run_every=crontab(minute='*/2'))
def import_hotel():
"""
runs hotel import every two minutes 
"""
	hotel_uri = 'hotel.csv'
	
	data = get_remote_content(URL+hotel_uri, USERNAME, PASSWORD)
	save_hotel(data)
	
