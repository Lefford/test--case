from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from maykin_case import hotels
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'maykin_case.views.home', name='home'),
    # url(r'^maykin_case/', include('maykin_case.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'', include('hotels.urls')),
)
