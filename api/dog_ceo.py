from core.request import Request
from requests import Response


class DogCeo:
    @staticmethod
    def breeds_list_all(url:str) -> Response:
        response = Request.get(f'{url}breeds/list/all')
        return response

    @staticmethod
    def breeds_image_random(url:str) -> Response:
        response = Request.get(f'{url}breeds/image/random')
        return response

    @staticmethod
    def breed_hound_images_random(url:str, num:int) -> Response:
        response = Request.get(f'{url}breed/hound/images/random/{num}')
        return response

    @staticmethod
    def breed_hound_image_random(url:str) -> Response:
        response = Request.get(f'{url}breed/hound/images/random')
        return response

    @staticmethod
    def breed_obj_images_random(url:str,obj:dict) -> Response:
        if obj.get('description'):
            response = Request.get(f'{url}breed/{obj["breed"]}/{obj["description"]}/images/random')
        else:
            response = Request.get(f'{url}breed/{obj["breed"]}/images/random')
        return response
