import autocomplete_light
from django.views.generic.base import TemplateView

autocomplete_light.autodiscover()

from django.conf.urls import include, url, patterns
from django.contrib import admin
import views


urlpatterns = patterns('',
	url(r'^search/$', 'termsearch.views.search'),
	url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
	url(r'^', 'termsearch.views.home'),
	)

