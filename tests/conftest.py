import os

import pytest

from core.load_data import load_json, load_csv
from root import ROOT_DIR
from core.logger import base_logger



@pytest.fixture(scope='session', autouse=True)
def setup_logger():
    base_logger.log_info("Start tests")

@pytest.fixture(scope='session')
def get_config():
    config = load_json(os.path.join(ROOT_DIR, 'config.json'))
    return config


@pytest.fixture
def get_data_dog_ceo(request):
    data = load_csv(os.path.join(ROOT_DIR, 'data', 'test_data', 'breeds.csv'))
    index = request.param
    return data[index]

