import requests

from core.logger import base_logger


class Request:
    @staticmethod
    def get(url, **kwargs):
        base_logger.log_debug(f'GET {url} {kwargs}')
        response = requests.get(url, **kwargs)
        base_logger.log_debug(f'{response.status_code} ')
        return response

    @staticmethod
    def post(url, **kwargs):
        base_logger.log_debug(f'POST {url} {kwargs}')
        response = requests.post(url, **kwargs)
        base_logger.log_debug(f'{response.status_code} {response.json()}')
        return response

    @staticmethod
    def put(url, **kwargs):
        base_logger.log_debug(f'PUT {url} {kwargs}')
        response = requests.put(url, **kwargs)
        base_logger.log_debug(f'{response.status_code} {response.json()}')
        return response

    @staticmethod
    def delete(url, **kwargs):
        base_logger.log_debug(f'DELETE {url} {kwargs}')
        response = requests.delete(url, **kwargs)
        base_logger.log_debug(f'{response.status_code}')
        return response
