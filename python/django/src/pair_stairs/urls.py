from django.conf.urls.defaults import patterns, include, url
from pair_stairs.stairs.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pair_stairs.views.home', name='home'),
    # url(r'^pair_stairs/', include('pair_stairs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^create/', create_stairs),
    url(r'^stairs/', view_stairs),
)
