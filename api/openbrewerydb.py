import os

from core.load_data import load_csv
from core.request import Request
from requests import Response
from core.dump_data import dump_json
from root import ROOT_DIR


class OpenBreweryDb:
    @staticmethod
    def get_breweries_num(url:str, per_page:int) -> Response:
        endpoint = f'breweries?per_page={per_page}'
        response = Request.get(f'{url}{endpoint}')
        dump_json(os.path.join(ROOT_DIR, 'data','outputdata','list_breweries.json'),response.json())
        return response

    @staticmethod
    def get_breweries_uuid(url, _uuid):
        endpoint = f'breweries/{_uuid}'
        response = Request.get(f'{url}{endpoint}')
        return response

    @staticmethod
    def get_breweries_random(url):
        endpoint = f'breweries/random'
        response = Request.get(f'{url}{endpoint}')
        return response

    @staticmethod
    def get_breweries_sort(url, key, value, per_page):
        endpoint = f'breweries/?{key}={value}&per_page={per_page}'
        response = Request.get(f'{url}{endpoint}')
        return response

    @staticmethod
    def get_value_key():
        data_list = load_csv(os.path.join(ROOT_DIR, 'data', 'test_data', 'openbrewerydb_sort_by.csv'))
        return data_list
