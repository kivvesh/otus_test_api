import os

from core.request import Request
from core.load_data import load_csv
from root import ROOT_DIR




class JsonPlaceHolder:
    @staticmethod
    def get_methods(url, endpoint):
        response = Request.get(url=f'{url}{endpoint}')
        return response

    @staticmethod
    def get_todos_num(url, num):
        endpoint = f'todos/{num}'
        response = Request.get(url=f'{url}{endpoint}')
        return response

    @staticmethod
    def get_data_from_config():
        data_list = load_csv(os.path.join(ROOT_DIR, 'data', 'test_data', 'jsonplaceholder.csv'))
        return data_list

    @staticmethod
    def get_posts_comments(url, num):
        endpoint = f'posts/{num}/comments'
        response = Request.get(url=f'{url}{endpoint}')
        return response
