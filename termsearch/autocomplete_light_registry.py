import autocomplete_light

autocomplete_light.autodiscover()

from models import *

#autocomplete_light.shortcuts.register(AirportInfo)
#autocomplete_light.shortcuts.register(AirportSearch)


class AirportSearchAutocomplete(autocomplete_light.AutocompleteModelBase):
    model = AirportSearch
    search_fields = ['both', 'location']
    attrs={'placeholder': 'your airport'}
   # choices = AirportSearch.objects.all()
#    choices = AirportSearch.objects.all()
#    widget = autocomplete_light.TextWidget()

class AirlineSearchAutocomplete(autocomplete_light.AutocompleteModelBase):
    model = AirlineSearch
    search_fields = ['airline']
    attrs={'placeholder': 'your airline'}

autocomplete_light.shortcuts.register(AirportSearch, AirportSearchAutocomplete)
autocomplete_light.shortcuts.register(AirlineSearch, AirlineSearchAutocomplete)




