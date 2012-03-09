from django.conf.urls.defaults import patterns, url, include
from django.conf import settings
from core.views import Home, VenueView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^$',  Home.as_view(), name='home'),
	url(r'^venue/$',  VenueView.as_view(), name='venue'),
    url(r'^mittun/', include('mittun.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # url(r'^pythonbrasil8/', include('pythonbrasil8.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
