from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    url(r"^$", 'srweb.frontend.views.home', name='home'),
    url(r'^frontend/', include('srweb.frontend.urls')),

)