from core.request import Request
from requests import Response
from core.logger import base_logger


class DogCeo:
    @staticmethod
    def breeds_list_all(url:str) -> Response:
        endpoint = 'breeds/list/all'
        response = Request.get(f'{url}{endpoint}')
        return response

    @staticmethod
    def breeds_image_random(url:str) -> Response:
        endpoint = 'breeds/image/random'
        response = Request.get(f'{url}{endpoint}')
        return response

    @staticmethod
    def breed_hound_images_random(url:str, num:int) -> Response:
        endpoint = f'breed/hound/images/random/{num}'
        response = Request.get(f'{url}{endpoint}')
        return response

    @staticmethod
    def breed_hound_image_random(url:str) -> Response:
        endpoint = 'breed/hound/images/random'
        response = Request.get(f'{url}{endpoint}')
        return response

    @staticmethod
    def breed_obj_images_random(url:str,obj:dict) -> Response:
        if obj.get('description'):
            response = Request.get(f'{url}breed/{obj["breed"]}/{obj["description"]}/images/random')
        else:
            response = Request.get(f'{url}breed/{obj["breed"]}/images/random')
        return response
