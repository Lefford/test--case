from hotels.forms import HotelForm
from hotels.models import Hotel, City
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

def home_view(request):
	return HttpResponse('Maykin test case')

def test_view(request):

	if request.is_ajax():
		city_value = request.GET.get('city')
		hotels_json = []
		if city_value:
			# get city based on made selection
			city = City.objects.get(code=city_value)
			
			# get the hotel based on selected city
			hotels_by_city = Hotel.objects.filter(city=city)
			# serialize the data 
			json_serializer = serializers.get_serializer("json")()
			hotels_json = json_serializer.serialize(hotels_by_city, ensure_ascii=False)		

		return HttpResponse(hotels_json, mimetype='JSON')
	else:
		# handle post and get
		form = HotelForm(request.POST or None)
		context_data = RequestContext(request, {'form': form, 'request': request})
		template_view = 'hotels/hotels.html'

		if form.is_valid():
			template_view = 'hotels/success.html'

		return render_to_response(template_view, context_data) 
