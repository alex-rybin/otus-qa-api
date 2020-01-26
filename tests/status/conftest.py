import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--url', action='store', default='https://ya.ru', help='Request URL'
    )
    parser.addoption(
        '--status_code', action='store', default=200, help='Expected HTTP status code'
    )


@pytest.fixture
def url_status_param(request):
    return {
        'url': request.config.getoption('--url'),
        'status_code': int(request.config.getoption('--status_code')),
    }
