import logging

import requests
from requests.exceptions import RequestException, Timeout, TooManyRedirects


logger = logging.getLogger('api')


class ChanApiError(Exception):
    pass


class ChanApi(object):

    base_url = 'a.4cdn.org'

    def __init__(self, resource):
        self.resource = resource

    def get_resource(self, *args):
        resource = self.resource if not args else self.resource.format(*args)

        url = 'http://{0}/{1}{2}'.format(self.base_url, resource, '.json')

        try:
            response = requests.get(url)
        except (RequestException, Timeout, TooManyRedirects) as exc:
            logger.critical(exc)
            raise ChanApiError('Unable to fetch {0}'.format(url))

        if response.ok:
            try:
                json = response.json()
            except Exception as exc:
                logger.critical(exc)
                raise ChanApiError('Invalid Json: {0}'.format(response.content))

        else:
            raise ChanApiError('Not OK - {0} - {1} - {2}'.format(
                url, response.status_code, response.content))

        return json

    @classmethod
    def get_thread(cls, board, thread_id):
        """
        Get thread of a board
        """
        return cls('{0}/thread/{1}').get_resource(*[board, thread_id])

    @classmethod
    def get_page(cls, board, page_number):
        """
        Get page of a board starting at 1
        """
        return cls('{0}/{1}').get_resource(*[board, page_number])

    @classmethod
    def get_catalog(cls, board):
        """
        Get catalog of all threads on a board
        """
        return cls('{0}/catalog').get_resource(*[board])

    @classmethod
    def get_threads(cls, board):
        """
        Get thread ids, modification times, respective pages of a board
        """
        return cls('{0}/threads').get_resource(*[board])

    @classmethod
    def get_archive(cls, board):
        """
        Get archived thread ids of a board
        """
        return cls('{0}/archive').get_resource(*[board])

    @classmethod
    def get_boards(cls):
        """
        Get all available boards
        """
        return cls('boards').get_resource()
