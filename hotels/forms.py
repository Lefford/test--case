from django import forms
from hotels.models import City, Hotel

class HotelForm(forms.Form):
	
	def __init__(self, *args, **kwargs):
		super(HotelForm, self).__init__(*args, **kwargs)

		# get initial value
		country_values = [(i.code, i.name) for i in City.objects.all()]
		city = City.objects.get(code='AMS')
		hotel_values = [(i.code, i.name) for i in Hotel.objects.filter(city=city)]

		# set field choices
		self.fields['city'] = forms.ChoiceField(choices=country_values)
		self.fields['hotels'] = forms.ChoiceField(choices=hotel_values)
