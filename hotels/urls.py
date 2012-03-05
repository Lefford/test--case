from django.conf.urls.defaults import patterns, include, url
from hotels.views import test_view, home_view, result_view

urlpatterns = patterns('',
     url(r'^$', home_view, name='home'),
     url(r'^test-form/$', test_view, name='choice-form'),
     url(r'^success/(\w+)/$', result_view, name='result'),
)
