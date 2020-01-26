import pytest
from requests import get, post


@pytest.mark.parametrize(
    'resource', ['posts', 'comments', 'albums', 'photos', 'todos', 'users']
)
def test_return_resource(resource):
    """
    Проверка, что при запросе ресурса возвращается не пустой список
    """
    response_json = get(f'https://jsonplaceholder.typicode.com/{resource}/').json()
    assert isinstance(response_json, list) and response_json


@pytest.mark.parametrize('id_', [1, 5, 8, 10, 99])
def test_post_id(id_):
    """
    Проверка совпадения ID у возвращённого поста с указанным в ссылке
    """
    response_json = get(f'https://jsonplaceholder.typicode.com/posts/{id_}/').json()
    assert response_json['id'] == id_


@pytest.mark.parametrize('id_', [1, 5, 8, 10, 99])
def test_comments_post_id(id_):
    """
    Проверка совпадения ID поста у возвращённых комментариев с указанным в ссылке
    """
    response_json = get(
        f'https://jsonplaceholder.typicode.com/comments?postId={id_}'
    ).json()
    assert all(comment['postId'] == id_ for comment in response_json)


def test_post_data():
    """
    Проверка наличия полей у комментариев
    """
    response_json = get('https://jsonplaceholder.typicode.com/comments').json()
    fields = ['postId', 'id', 'name', 'email', 'body']
    assert all(list(comment.keys()) == fields for comment in response_json)


@pytest.mark.parametrize('id_', range(1, 11))
def test_create_post_user_id(id_):
    """
    Проверка совпадения ID у созданного поста с указанным в ссылке
    """
    sample_post = {'title': 'foo', 'body': 'bar', 'userId': id_}
    response_json = post(
        'https://jsonplaceholder.typicode.com/posts', json=sample_post
    ).json()
    assert response_json['userId'] == id_
