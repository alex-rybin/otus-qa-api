import pytest
from requests import get


def test_return_breweries_list():
    """
    Проверка, что по умолчанию возвращается список из 20 элементов
    """
    response_json = get('https://api.openbrewerydb.org/breweries').json()
    assert isinstance(response_json, list) and len(response_json) == 20


@pytest.mark.parametrize(
    'city', ['New York', 'Boston', 'Chicago', 'Seattle', 'Portland']
)
def test_filter_by_city(city):
    """
    Проверка работы фильтра по городу
    """
    response_json = get(
        f'https://api.openbrewerydb.org/breweries?by_city={city.lower().replace(" ", "_")}'
    ).json()
    assert all(city in brewery['city'] for brewery in response_json)


@pytest.mark.parametrize('per_page', range(5, 11))
def test_page_length(per_page):
    """
    Проверка, что параметр per_page меняет количество элементов на странице
    """
    response_json = get(
        f'https://api.openbrewerydb.org/breweries?per_page={per_page}'
    ).json()
    assert len(response_json) == per_page


@pytest.mark.parametrize('type_', ['micro', 'regional', 'bar', 'large', 'contract'])
def test_filter_by_type(type_):
    """
    Проверка работы фильтра по типу
    """
    response_json = get(
        f'https://api.openbrewerydb.org/breweries?by_type={type_}'
    ).json()
    assert all(type_ == brewery['brewery_type'] for brewery in response_json)


@pytest.mark.parametrize(
    'tag', ['dog-friendly', 'patio', 'food-service', 'food-truck', 'tours']
)
def test_filter_by_tag(tag):
    """
    Проверка работы фильтра по тегу
    """
    response_json = get(f'https://api.openbrewerydb.org/breweries?by_tag={tag}').json()
    assert all(tag in brewery['tag_list'] for brewery in response_json)
