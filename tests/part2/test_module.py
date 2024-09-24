import pytest

from core.request import Request


@pytest.mark.test_module
@pytest.mark.smoke
def test_module(url_status):
    url, status = url_status
    response = Request.get(url)
    assert response.status_code == int(status)
