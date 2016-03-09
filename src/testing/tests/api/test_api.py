import mock
import pytest
import requests
from requests.exceptions import RequestException

from banter.api import ChanApi, ChanApiError


class TestChanApi(object):

    def setup(self):
        self.api = ChanApi('foo')

        self.response_mock = requests.models.Response()
        self.response_mock.status_code = 200
        self.response_mock._content = b'{"data": []}'

    @mock.patch('requests.get')
    def test_get_resource_requests_exception(self, get_mock):
        get_mock.side_effect = RequestException('Something went wrong')

        with pytest.raises(ChanApiError) as exc:
            self.api.get_resource()

        assert 'Unable to fetch' in str(exc)

    @mock.patch('requests.get')
    def test_get_resource_json_exception(self, get_mock):
        response = requests.models.Response()
        response.status_code = 200
        response._content = '{"foo": "bar"}'
        get_mock.return_value = response

        with pytest.raises(ChanApiError) as exc:
            self.api.get_resource()

        assert 'Invalid Json' in str(exc)

    @mock.patch('requests.get')
    def test_get_resource_response_not_ok(self, get_mock):
        response = requests.models.Response()
        response.status_code = 404
        response._content = 'Not Found'
        get_mock.return_value = response

        with pytest.raises(ChanApiError) as exc:
            self.api.get_resource()

        assert '404 - Not Found' in str(exc)

    @mock.patch('requests.get')
    def test_success_call(self, get_mock):
        get_mock.return_value = self.response_mock

        # no args
        api = ChanApi('foo')
        api.get_resource()
        get_mock.assert_called_with('http://a.4cdn.org/foo.json')

        # args
        api = ChanApi('foo/{0}')
        api.get_resource(1)
        get_mock.assert_called_with('http://a.4cdn.org/foo/1.json')

    @mock.patch('requests.get')
    def test_get_thread(self, get_mock):
        get_mock.return_value = self.response_mock

        ChanApi.get_thread('g', '1')

        get_mock.assert_called_with('http://a.4cdn.org/g/thread/1.json')

    @mock.patch('requests.get')
    def test_get_page(self, get_mock):
        get_mock.return_value = self.response_mock

        ChanApi.get_page('g', '6')

        get_mock.assert_called_with('http://a.4cdn.org/g/6.json')

    @mock.patch('requests.get')
    def test_get_catalog(self, get_mock):
        get_mock.return_value = self.response_mock

        ChanApi.get_catalog('g')

        get_mock.assert_called_with('http://a.4cdn.org/g/catalog.json')

    @mock.patch('requests.get')
    def test_get_threads(self, get_mock):
        get_mock.return_value = self.response_mock

        ChanApi.get_threads('g')

        get_mock.assert_called_with('http://a.4cdn.org/g/threads.json')

    @mock.patch('requests.get')
    def test_get_archive(self, get_mock):
        get_mock.return_value = self.response_mock

        ChanApi.get_archive('g')

        get_mock.assert_called_with('http://a.4cdn.org/g/archive.json')

    @mock.patch('requests.get')
    def test_get_boards(self, get_mock):
        get_mock.return_value = self.response_mock

        ChanApi.get_boards()

        get_mock.assert_called_with('http://a.4cdn.org/boards.json')
