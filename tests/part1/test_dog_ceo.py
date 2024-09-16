import pytest
import os

from api.dog_ceo import DogCeo
from core.asserts import Assert
from core.dump_data import dump_json
from root import ROOT_DIR

@pytest.mark.dog_ceo
def test_get_breeds_list_all(get_config):
    url = get_config['dog.ceo']['url']
    response = DogCeo.breeds_list_all(url)
    Assert.assert_status_code(response)
    Assert.assert_isistance(response.json(), dict)
    dump_json(os.path.join(ROOT_DIR,'data','list_breeds.json'),response.json()['message'])

