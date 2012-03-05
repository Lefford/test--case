from hotels.forms import HotelForm
from hotels.models import Hotel, City
from django.core.urlresolvers import reverse
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

def home_view(request, template_view='hotels/hotels.html'):
	return render_to_response('hotels/home.html')

def result_view(request, hotel_code, template_view='hotels/succes.html'):
	hotel = Hotel.objects.get(code=hotel_code)

	return render_to_response(template_view, {'hotel_name': hotel.name, 'city_name': hotel.city.name})

	
def test_view(request, template_view='hotels/hotels.html'):
	if request.is_ajax():
		hotels_json = []
		city_value = request.GET.get('city')
		if city_value:
			# get city based on form selection
			city = City.objects.get(code=city_value)
			
			# get the hotel based on selected city
			hotels_by_city = Hotel.objects.filter(city=city)
			
			# serialize the data 
			json_serializer = serializers.get_serializer("json")()
			hotels_json = json_serializer.serialize(hotels_by_city, ensure_ascii=False)		

		return HttpResponse(hotels_json, mimetype='JSON')
	else:
		# handle post and get request
		form = HotelForm(request.POST or None, request=request)
		context_data = RequestContext(request, {'form': form})
		
		if form.is_valid():
			hotel_choice 	= form.cleaned_data['hotels']
			
			return HttpResponseRedirect(reverse('result', args=(hotel_choice,)))

		return render_to_response(template_view, context_data) 
