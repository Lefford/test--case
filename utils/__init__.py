import urllib2, base64
import re 

def get_remote_content(url, username, password):
	""" 
	import csv remotely
	"""	
	
	data= None		
	try:
		request = urllib2.Request(url)
		login_cred = base64.encodestring('{0}:{1}'.format(username, password))
		request.add_header('Authorization', 'Basic {0}'.format(login_cred))
		
		csv_file = urllib2.urlopen(request)
		data = _format_data(csv_file)
		
		data.update({'response_code': csv_file.code})
	except urllib2.URLError as e:
		print 'Error message: {0}'.format(e)

	return data

def _format_data(a_file):
	data = ''
	for line in a_file:
		data+= line

	return {'data': data}
 
def get_local_content(path):
	"""
	Import csv locally
	"""

	data=None
	try:
		csv_file = open(path)
		data = _format_data(csv_file)
	except IOError as e:
		print e

	return data

def clean_data(line, separator=';'):
	"""
	Get character between "<char>"
	"""
	return map(lambda x: re.search(r'"(.+)"', x).group(1), re.split(separator, line)) 
