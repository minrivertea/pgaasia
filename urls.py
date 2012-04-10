from django.conf.urls import patterns, include, url
import django.views.static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from registration.views import register

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'website.views.home', name='home'),
    # url(r'^website/', include('website.foo.urls')),
    (r'^forum/', include('pybb.urls', namespace='pybb')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^accounts/register/$', register,
        {'backend': 'website.regbackend.RegBackend',},        
        name='registration_register'
    ),

    (r'^accounts/', include('registration.backends.default.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += staticfiles_urlpatterns()

