from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from banter.core.views import IndexView

admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^api/', include('banter.api.urls', namespace='api')),
]

if settings.DEBUG:
    urlpatterns += [
        url(
            r'^%s(?P<path>.*)$' % settings.MEDIA_URL.strip('/'),
            'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}
        ),
    ]
