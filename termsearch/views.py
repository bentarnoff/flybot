from django.shortcuts import render, render_to_response
from models import *
from django.http import HttpResponse, HttpResponseRedirect
import sys

import autocomplete_light

autocomplete_light.autodiscover()
from forms import *

def flip_term(departures):
	dep_terms = ("International", "North", "South", "West", "Commuter", "Interisland", "Main")
	if departures in dep_terms:
		return True
	else:
		return False

def home(request):
	error = False
	airport_search = AirportSearchForm()
	airline_search = AirlineSearchForm()
	return render_to_response("index.html", {'airport_search': airport_search, 'airline_search': airline_search})

def search(request):
	if request.method == 'GET':
		airport_results = AirportSearchForm(request.GET)
		airline_results = AirlineSearchForm(request.GET)
		if airport_results.is_valid() and airline_results.is_valid():
			try:
				port = airport_results.cleaned_data['airport_input']
				line = airline_results.cleaned_data['airline_input']

				a = AirportInfo.objects.get(pk=port)
				b = str(a)
				b_list = b.split(", ")
				port_code = b_list[0]
				port = b_list[1]

				c = AirlineSearch.objects.get(pk=line)
				line = c

				port_code = port_code.lower()
				port_code = port_code.capitalize()

				z = getattr(sys.modules[__name__], port_code)

				message = z.objects.filter(airline__contains=line)

				d = str(message)
				msg_list = d.split(",")
				departures = msg_list[2]
				term_or_con = msg_list[4]

				flip = False

				if flip_term(departures):
					flip = True

				return render_to_response("search.html", {'flip': flip, 'departures': departures, 'line': line, 'port': port, 'term_or_con': term_or_con})
	
			except (IndexError, AttributeError, ValueError) as e:
				airport_search = AirportSearchForm()
				airline_search = AirlineSearchForm()
				return render_to_response("index.html", {'error': True, 'airport_search': airport_search, 'airline_search': airline_search})
		else:
			airport_search = AirportSearchForm()
			airline_search = AirlineSearchForm()
			return render_to_response("index.html", {'error': True, 'airport_search': airport_search, 'airline_search': airline_search})
