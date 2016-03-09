from django.http import JsonResponse
from django.conf import settings
from django.views.generic import View
from django.utils.html import strip_tags
from django.template.defaultfilters import truncatechars

from .api import ChanApi


class BoardListView(View):

    def get(self, request, *args, **kwargs):
        return JsonResponse(settings.BOARD_LIST, safe=False)


class CatalogView(View):

    def get(self, request, *args, **kwargs):
        catalog = ChanApi.get_catalog(kwargs.get('board'))
        for page in catalog:
            for thread in page['threads']:
                subject = thread.get('sub')
                comment = thread.get('com')

                thread['title'] = strip_tags(subject) if subject else ''
                thread['comment'] = truncatechars(strip_tags(comment), 180) if comment else ''
        return JsonResponse(catalog, safe=False)


class ThreadDetailView(View):

    def get(self, request, *args, **kwargs):
        board = kwargs.get('board')
        _id = kwargs.get('id')

        posts = ChanApi.get_thread(board, _id)
        return JsonResponse(posts, safe=False)
