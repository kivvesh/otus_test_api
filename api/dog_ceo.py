from core.request import Request


class DogCeo:
    @staticmethod
    def breeds_list_all(url):
        response = Request.get(f'{url}breeds/list/all')
        return response

    @staticmethod
    def breeds_image_random(url):
        response = Request.get(f'{url}breeds/image/random')
        return response

    @staticmethod
    def breed_hound_images_random(url, num):
        response = Request.get(f'{url}breed/hound/images/random/{num}')
        return response
