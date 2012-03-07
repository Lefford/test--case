from django import forms
from hotels.models import City, Hotel

class HotelForm(forms.Form):
	
	def __init__(self, *args, **kwargs):
		request = kwargs.pop('request', None)
		super(HotelForm, self).__init__(*args, **kwargs)

		# get the city for hotels
		city_code = request.POST.get('cities', None)
		try:
			city = City.objects.get(code=city_code)
		except City.DoesNotExist:
			city = City.objects.get(code='AMS')
		
		# selectbox value
		hotel_values = [(i.code, i.name) for i in Hotel.objects.filter(city=city)]
		country_values = [(i.code, i.name) for i in City.objects.all()]

		# set field choices
		self.fields['cities'] = forms.ChoiceField(choices=country_values)
		self.fields['hotels'] = forms.ChoiceField(choices=hotel_values)
		