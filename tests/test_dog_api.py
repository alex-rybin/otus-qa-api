import pytest
from requests import get


def test_random_image_accessible():
    """
    Проверка доступности случайного изображения
    """
    response = get('https://dog.ceo/api/breeds/image/random')
    response_picture = get(response.json()['message'])
    assert response_picture.status_code == 200


@pytest.mark.parametrize('count', range(1, 6))
def test_random_images_count(count):
    """
    Проверка совпадения количества запрошенных изображений с указанным числом
    """
    response = get(f'https://dog.ceo/api/breeds/image/random/{count}')
    assert len(response.json()['message']) == count


@pytest.mark.parametrize(
    'breed', ['borzoi', 'buhund', 'germanshepherd', 'corgi', 'husky']
)
def test_return_correct_breed_path(breed):
    """
    Проверка наличия названия породы во всех ссылках на изображения из ответа
    """
    response = get(f'https://dog.ceo/api/breed/{breed}/images')
    assert all(breed in link for link in response.json()['message'])


@pytest.mark.parametrize(
    'subbreed',
    [
        'buhund/norwegian',
        'bulldog/english',
        'bullterrier/staffordshire',
        'cattledog/australian',
        'deerhound/scottish',
    ],
)
def test_return_correct_subbreed_path(subbreed):
    """
    Проверка наличия названия суб-породы во всех ссылках на изображения из ответа
    """
    response = get(f'https://dog.ceo/api/breed/{subbreed}/images')
    assert all(
        subbreed.replace('/', '-') in link for link in response.json()['message']
    )


def test_return_error_for_nonexistent_breed():
    """
    Проверка наличия сообщения об ошибке при отсутствии породы
    """
    response = get('https://dog.ceo/api/breed/dogewow/images')
    assert response.json()['message'] == 'Breed not found (master breed does not exist)'
