import os
import time
import pytest

from core.load_data import load_json, load_csv
from root import ROOT_DIR
from core.logger import base_logger
from api.gectaro import Gectaro


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default='https://ya.ru', help="URL to test")
    parser.addoption("--status_code", action="store", default=200, help="Expected status code")


@pytest.fixture(scope='session', autouse=True)
def setup_logger():
    base_logger.log_info("Start tests")
    start = time.time()
    yield
    base_logger.log_info(f"Start finish\ntest running time: {round(time.time() - start,2)} сек")

@pytest.fixture(scope='session')
def get_config():
    config = load_json(os.path.join(ROOT_DIR, 'config.json'))
    return config


@pytest.fixture()
def get_data_dog_ceo(request):
    data = load_csv(os.path.join(ROOT_DIR, 'data', 'test_data', 'breeds.csv'))
    index = request.param
    return data[index]


@pytest.fixture(scope='function')
def get_data_breweries():
    data = load_json(os.path.join(ROOT_DIR, 'data', 'outputdata', 'list_breweries.json'))
    return data


@pytest.fixture
def url_status(request):
    url = request.config.getoption('--url', default='https://ya.ru')
    status_code = request.config.getoption('--status_code', default=200)
    return url, status_code


@pytest.fixture
def get_id_project(get_config):
    return get_config.get('gectaro').get('id_project')


@pytest.fixture()
def get_project_tasks_resource_id(get_config, get_id_project):
    url = get_config.get('gectaro').get('url')
    token = get_config.get('gectaro').get('token')
    response = Gectaro.get_resource_requests(url, token, get_id_project)
    return [int(resource['project_tasks_resource_id']) for resource in response.json()]


@pytest.fixture()
def get_id_resource(get_config, get_id_project):
    url = get_config.get('gectaro').get('url')
    token = get_config.get('gectaro').get('token')
    response = Gectaro.get_resource_requests(url, token, get_id_project)
    return [int(resource['id']) for resource in response.json()]

@pytest.fixture()
def get_resource(get_config, get_id_project):
    url = get_config.get('gectaro').get('url')
    token = get_config.get('gectaro').get('token')
    response = Gectaro.get_resource_requests(url, token, get_id_project)
    return [resource for resource in response.json()]