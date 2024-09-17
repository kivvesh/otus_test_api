import os.path

import pytest

from core.load_data import load_json
from root import ROOT_DIR


@pytest.fixture(scope='session')
def get_config():
    config = load_json(os.path.join(ROOT_DIR, 'config.json'))
    return config
