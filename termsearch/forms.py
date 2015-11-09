from django import forms

import autocomplete_light
autocomplete_light.autodiscover()

from models import *

class AirportSearchForm(forms.Form):
	airport_input = autocomplete_light.ChoiceField('AirportSearchAutocomplete', label="")	

class AirlineSearchForm(forms.Form):
	airline_input = autocomplete_light.ChoiceField('AirlineSearchAutocomplete', label="")