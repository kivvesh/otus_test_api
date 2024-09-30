from random import randint

import pytest

from api.gectaro import Gectaro
from core.asserts import Assert
from models.gectaro import ResourseResponse, ResourseRequest


@pytest.mark.gectaro
def test_get_companies(get_config):
    url = get_config.get('gectaro').get('url')
    token = get_config.get('gectaro').get('token')
    response = Gectaro.get_companies(url, token)
    Assert.assert_status_code(response, 200)


@pytest.mark.parametrize(
    'project_id,status',
    [
        (2, 404),
        (2, 401),
        (100, 403),
    ]
)
@pytest.mark.gectaro
def test_negative_get_resource_requests(get_config, project_id, status):
    url = get_config.get('gectaro').get('url')
    token = '' if status == 401  else get_config.get('gectaro').get('token')
    response = Gectaro.get_resource_requests(url, token, project_id)
    Assert.assert_status_code(response, status)


@pytest.mark.gectaro
def test_get_resource_requests(get_config, get_id_project):
    url = get_config.get('gectaro').get('url')
    token = get_config.get('gectaro').get('token')
    response = Gectaro.get_resource_requests(url, token, get_id_project)
    Assert.assert_status_code(response, 200)
    for obj in response.json():
        Assert.assert_correct_model(obj, ResourseResponse)


@pytest.mark.parametrize(
    'volume,cost,needed_at,status',
    [
        (12,'dsf',23423342234,422),
        (10,15,2123,422),
        (10,15,-2123,422),
        (12,'1f5',2123,422),
        (-11,23,2123,422),
        (11,-23,2123,422),
        (10,23,1731070093,201),
    ]
)
@pytest.mark.gectaro
def test_post_resource_requests(
        get_config, get_project_tasks_resource_id,
        volume,cost,needed_at,status, get_id_project
):
    project_tasks_resource_id = get_project_tasks_resource_id[randint(0,len(get_project_tasks_resource_id)-1)]
    url = get_config.get('gectaro').get('url')
    token = get_config.get('gectaro').get('token')
    data = ResourseRequest(
        project_tasks_resource_id=project_tasks_resource_id,
        volume=volume,
        cost=cost,
        needed_at=needed_at
    ).model_dump()
    response = Gectaro.post_resource_requests(url, token, get_id_project, data)
    Assert.assert_status_code(response, status)


@pytest.mark.parametrize(
    'status',
    [
        (200) for i in range(10)
    ]
)
@pytest.mark.gectaro
@pytest.mark.smoke
def test_get_resource_requests_id(get_config, get_id_project, get_id_resource, status):
    url = get_config.get('gectaro').get('url')
    token = get_config.get('gectaro').get('token')
    id = get_id_resource[randint(0,len(get_id_resource)-1)]
    response = Gectaro.get_resource_requests_id(url, token,get_id_project,id)
    Assert.assert_status_code(response, status)
    Assert.assert_correct_model(response.json(), ResourseResponse)

