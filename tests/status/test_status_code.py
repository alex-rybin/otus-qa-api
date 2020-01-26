from requests import get


def test_response_status(url_status_param):
    """
    Проверка на совпадение кода ответа сервера с ожидаемым
    """
    response = get(url_status_param['url'])
    assert response.status_code == url_status_param['status_code']
