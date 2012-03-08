from django.db import IntegrityError
from optparse import  make_option
from django.core.management.base import BaseCommand, CommandError
from utils import get_remote_content, get_local_content, clean_data
from hotels.models import City, Hotel

class Command(BaseCommand):
	option_list = BaseCommand.option_list + (
        	make_option('--local', '-l', dest='local',
	            help='The local import a local file.'),
	    )

	args = 'URL username password'
	help = 'Import resource on a remote site'

	def handle(self, *args, **options):
		path = options.get('local')
		city_data = None

		if path:
			city_data = get_local_content(path)
		else:
			if len(args) < 3:
				raise CommandError('Insert URL username password')

			city_data = get_remote_content(args[0], args[1], args[2])
		
		save_hotel(city_data['data'])

def save_hotel(data):
	"""
	Parse data and save a hotel instance if not exist.
	"""
	# split the string on new line symbols 
	data = data.split('\n')
	temp_hotel = None
	count_new_obj = 0
	for line in data:
		parsed_data = clean_data(line)
		if parsed_data:
			try:
				city = City.objects.get(code=parsed_data[0])
				temp_hotel = Hotel()
				temp_hotel.city = city
				temp_hotel.code = parsed_data[1]
				temp_hotel.name = parsed_data[2]
				temp_hotel.save()
				count_new_obj+=1
			except IntegrityError, Hotel.DoesNotExist:
				pass	

	print '{0} new hotels added'.format(count_new_obj)
