from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    url(r"^data$", 'srweb.frontend.views.data', name='connectivity'),
)