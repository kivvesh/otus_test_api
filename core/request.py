import requests


class Request:
    @staticmethod
    def get(url, **kwargs):
        response = requests.get(url, **kwargs)
        return response

    @staticmethod
    def post(url, **kwargs):
        response = requests.post(url, **kwargs)
        return response
