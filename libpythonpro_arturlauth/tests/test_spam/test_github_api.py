from unittest.mock import Mock

import pytest

from libpythonpro_arturlauth import github_api


@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars2.githubusercontent.com/u/63745619?v=4'
    resp_mock.json.return_value = {'login': 'arturlauth', 'id': 63745619,
                                   'avatar_url': url, }
    get_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = get_original


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('arturlauth')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('renzo')
    assert 'https://avatars3.githubusercontent.com/u/402714?v=4' == url
