from core.request import Request

class DogCeo:
    @staticmethod
    def breeds_list_all(url):
        response = Request.get(f'{url}breeds/list/all')
        return response
