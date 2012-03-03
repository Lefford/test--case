from django.conf.urls.defaults import patterns, include, url
from hotels.views import test_view, home_view

urlpatterns = patterns('',
     url(r'^$', home_view, name='home-view'),
     url(r'^test-form/$', test_view, name='test-form') 
)
