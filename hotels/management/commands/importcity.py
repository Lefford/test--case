from django.db import IntegrityError
from optparse import  make_option
from django.core.management.base import BaseCommand, CommandError
from utils import get_remote_content, get_local_content, clean_data
from hotels.models import City

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

		save_city(city_data)

def save_city(city_data):
	"""
	This function parsed the line and save a city in database.
	"""
# split the string on new line symbols 
	city_data = city_data.split('\n')
	temp_city = None
	count_new_obj = 0
	for line in city_data:
		parsed_data = clean_data(line)
		if parsed_data:
			try:
				temp_city = City()
				temp_city.code = parsed_data[0]
				temp_city.name = parsed_data[1]
				temp_city.save()
				count_new_obj+= 1
			except IntegrityError:
				pass

	print '{0} new cities added'.format(count_new_obj)
