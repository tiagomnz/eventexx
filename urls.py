# -*- coding: utf8 -*-
from django.conf.urls.defaults import patterns
from core.views import homepage
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', homepage),

    # Examples:
    # url(r'^$', 'eventexx.views.home', name='home'),
    # url(r'^eventexx/', include('eventexx.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
