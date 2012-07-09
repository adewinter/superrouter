from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'srweb.frontend.views.connectivity', name='home'),
#    url(r'^$', include('srweb.frontend.urls')),
    url(r"^connectivity/$", 'srweb.frontend.views.connectivity', name='connectivity'),
    url(r"^settings/$", 'srweb.frontend.views.settings', name='settings'),
    url(r"^media/$", 'srweb.frontend.views.media', name='media'),
    url(r"^advanced/$", 'srweb.frontend.views.advanced', name='advanced'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
