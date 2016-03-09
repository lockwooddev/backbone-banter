from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page

from .views import BoardListView, CatalogView, ThreadDetailView


urlpatterns = patterns('',
    url(r'^boards/$', BoardListView.as_view(), name='board_list'),

    url(r'^boards/(?P<board>[-_\w]+)/catalog/$',
        cache_page(60 * 60)(CatalogView.as_view()), name='board_catalog'),

    url(r'^boards/(?P<board>[-_\w]+)/threads/(?P<id>[-_\w]+)$',
        cache_page(60 * 60)(ThreadDetailView.as_view()), name='thread_detail'),
)
