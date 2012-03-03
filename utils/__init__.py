import urllib2, base64, urllib2
import re 

def get_remote_content(url, username, password):
	""" 
	import cvs remotely
	"""	
		
	data = ''

	try:
		request = urllib2.Request(url)
		login_cred = base64.encodestring('{0}:{1}'.format(username, password)).replace('\n', '')
		request.add_header('Authorization', 'Basic {0}'.format(login_cred))
		
		# we may be dealing with a huge mf
		csv_file = urllib2.urlopen(request)
		for line in csv_file:
			data+= line

	except urllib2.URLError as e:
		print 'Error message: {0}'.format(e)

	return data

def get_local_content(path):
	"""
	Import csv locally
	"""
	data = '' 
	try:
		cvs_file = open(path)
		data = cvs_file.read() 
		
		# write the line in pieces a string, you dont know how big a file may be
		for line in data:
			data+= line

	except IOError:
		pass

	return data

def clean_data(line, separator=';'):
	"""
	Parse line from cvs file
	"""
	
	cleaned_data = []

	# get value from sequence
	for value in line.split(separator):
		parsed_data = re.search(r'"(.+)"', value)
		if parsed_data:
			# get regex selection, name 
			parsed_data = parsed_data.group(1)
			cleaned_data.append(parsed_data)
	return cleaned_data
