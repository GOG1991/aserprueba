from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aser.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^',include('home.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^servicios/',include('servicios.urls')),
    url(r'^clientes/',include('clientes.urls')),
    url('',include('equipos.urls')),
    url('',include('historiales.urls')),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += patterns('',
             url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),)