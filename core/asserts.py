from requests import Response


class Assert:
    @staticmethod
    def assert_status_code(response: Response, code:int):
        assert response.status_code == code

    @staticmethod
    def assert_is_istance(obj, type_obj):
        assert isinstance(obj, type_obj)

    @staticmethod
    def assert_in_json(response:Response, key:str):
        assert response.json().get(key)

    @staticmethod
    def assert_len_number(response: Response, num: int):
        assert len(response.json()['message']) == num
