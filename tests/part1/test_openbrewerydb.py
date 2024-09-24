import pytest
import os

from api.openbrewerydb import OpenBreweryDb
from core.asserts import Assert
from core.load_data import load_json, load_csv
from root import ROOT_DIR
from models.openbrewerydb import Brewery


@pytest.mark.openbrewerydb
@pytest.mark.smoke
def test_get_breweries_num(get_config):
    """Test breweries?per_page={per_page}"""
    url = get_config['openbrewerydb']['url']
    per_page = get_config['openbrewerydb']['per_page']
    response = OpenBreweryDb.get_breweries_num(url, per_page)
    Assert.assert_status_code(response, 200)
    [Assert.assert_correct_model(obj, Brewery) for obj in response.json()]


@pytest.mark.parametrize(
    'uuid,status_code',
    [(i['id'],200)
     for i in load_json(os.path.join(ROOT_DIR, 'data', 'outputdata', 'list_breweries.json'))]
)
@pytest.mark.openbrewerydb
@pytest.mark.smoke
def test_get_breweries_uuid(get_config,uuid,status_code):
    """Test breweries/{_uuid}"""
    url = get_config['openbrewerydb']['url']
    response = OpenBreweryDb.get_breweries_uuid(url, uuid)
    Assert.assert_status_code(response, status_code)
    Assert.assert_correct_model(response.json(), Brewery)


@pytest.mark.parametrize(
    'key,value,status_code',
    [(key, value, 200) for obj in OpenBreweryDb.get_value_key()
     for key, value in obj.items()]
)
@pytest.mark.openbrewerydb
@pytest.mark.smoke
def test_get_breweries_sort(get_config,key, value, status_code):
    """Test for sorting"""
    url = get_config['openbrewerydb']['url']
    per_page = get_config['openbrewerydb']['per_page']
    response = OpenBreweryDb.get_breweries_sort(url, key,value,per_page)
    Assert.assert_status_code(response,status_code)
    [Assert.assert_correct_model(obj, Brewery) for obj in response.json()]



@pytest.mark.openbrewerydb
@pytest.mark.smoke
def test_get_breweries_random(get_config):
    """Random response test"""
    url = get_config['openbrewerydb']['url']
    per_page = get_config['openbrewerydb']['per_page']
    id_response = []
    for number in range(per_page):
        response = OpenBreweryDb.get_breweries_random(url)
        response_json = response.json()
        Assert.assert_status_code(response, 200)
        Assert.assert_correct_model(response_json[0],Brewery)
        id_response.append(response_json[0]['id'])
    assert len(set(id_response)) > 1