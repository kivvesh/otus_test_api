from requests import Response


class Assert:
    @staticmethod
    def assert_status_code(response: Response):
        assert response.status_code == 200

    @staticmethod
    def assert_isistance(obj, type_obj):
        assert isinstance(obj, type_obj)
