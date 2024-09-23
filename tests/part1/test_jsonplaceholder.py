import pytest

from api.jsonplaceholder import JsonPlaceHolder
from core.asserts import Assert


@pytest.mark.jsonplaceholder
@pytest.mark.parametrize(
    'endpoint,count,response',
    [(obj['endpoint'],obj['count'],obj['response'])
    for obj in JsonPlaceHolder.get_data_from_config()]
)
def test_get_methods(get_config, endpoint,count,response):
    url = get_config['jsonplaceholder']['url']
    response = JsonPlaceHolder.get_methods(url, endpoint)
    Assert.assert_status_code(response, response.status_code)
    Assert.assert_correct_count(response, count)


@pytest.mark.jsonplaceholder
@pytest.mark.parametrize(
    'num,status_code',
    [(num, 200) for num in range(1,10)]
)
def test_get_todos_num(get_config, num, status_code):
    url = get_config['jsonplaceholder']['url']
    response = JsonPlaceHolder.get_todos_num(url, num)
    Assert.assert_status_code(response, status_code)
