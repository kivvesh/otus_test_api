from requests import Response
from pydantic import ValidationError


class Assert:
    @staticmethod
    def assert_status_code(response: Response, code:int):
        assert response.status_code == code

    @staticmethod
    def assert_is_instance(obj, type_obj):
        assert isinstance(obj, type_obj)

    @staticmethod
    def assert_in_json(response:Response, key:str):
        assert response.json().get(key)

    @staticmethod
    def assert_len_number(response: Response, num: int):
        assert len(response.json()['message']) == num

    @staticmethod
    def assert_correct_model(obj: dict, model):
        try:
            assert model(**obj)
        except ValidationError as e:
            assert model(**obj), e

    @staticmethod
    def assert_correct_count(response: Response, count:int):
        assert len(response.json()) == int(count)