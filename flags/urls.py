from django.conf.urls import patterns, url

urlpatterns = patterns('flags.views',
    url(r'^create/$', 'flag_create', name='flag_create'),
)
