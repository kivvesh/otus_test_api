import pytest
import os

from api.dog_ceo import DogCeo
from core.asserts import Assert
from core.dump_data import dump_json
from root import ROOT_DIR


@pytest.mark.dog_ceo
def test_get_breeds_list_all(get_config):
    """Test breeds/list/all"""
    url = get_config['dog.ceo']['url']
    response = DogCeo.breeds_list_all(url)
    Assert.assert_status_code(response, 200)
    Assert.assert_is_instance(response.json(), dict)
    dump_json(os.path.join(ROOT_DIR, 'data', 'outputdata', 'list_breeds.json'), response.json()['message'])


@pytest.mark.dog_ceo
def test_get_breeds_image_random(get_config):
    """Test breeds/image/random"""
    url = get_config['dog.ceo']['url']
    response = DogCeo.breeds_image_random(url)
    Assert.assert_status_code(response, 200)
    Assert.assert_in_json(response, 'message')


@pytest.mark.dog_ceo
@pytest.mark.parametrize(
    'num,len_num,status_code',
    [
        (5, 5, 200),
        (10, 10, 200)
    ]
)
def test_breed_hound_images_random(num, len_num, status_code, get_config):
    """breed/hound/images/random/{num}"""
    url = get_config['dog.ceo']['url']
    response = DogCeo.breed_hound_images_random(url, num)
    Assert.assert_status_code(response, status_code)
    Assert.assert_len_number(response, len_num)


@pytest.mark.dog_ceo
@pytest.mark.parametrize(
    'get_data_dog_ceo', range(4), indirect=True,
    ids=[f'index:{index}' for index in range(4)]
)
def test_breed_hound_image_random(get_config, get_data_dog_ceo):
    url = get_config['dog.ceo']['url']
    response = DogCeo.breed_obj_images_random(url, get_data_dog_ceo)
    Assert.assert_status_code(response, int(get_data_dog_ceo['status']))
