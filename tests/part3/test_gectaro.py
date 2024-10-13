import pytest

from random import randint

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


@pytest.mark.parametrize(
    'volume,cost,status,is_over_budget',
    [
        (100,100,200, 1),
        (100,None,200, 1),
        (None,100,200, 1),
        (None,None,200, 1),
        (-400,1234,200, 1),
        (-400,'dsfsd',422, 1),
        ('sdfsd',500,422, 1),
    ]
)
@pytest.mark.gectaro
@pytest.mark.smoke
def test_put_resource_requests_id(get_config, get_id_project,is_over_budget,
    get_project_tasks_resource_id,volume,cost,status, get_id_resource):
    url = get_config.get('gectaro').get('url')
    token = get_config.get('gectaro').get('token')
    project_tasks_resource_id = get_project_tasks_resource_id[randint(0,len(get_project_tasks_resource_id)-1)]
    id = get_id_resource[randint(0, len(get_id_resource) - 1)]
    data = {
        'project_tasks_resource_id': project_tasks_resource_id,
        'volume': volume,
        'cost': cost,
        'is_over_budget': is_over_budget,
    }
    response = Gectaro.put_resource_requests_id(url, token,get_id_project, id, data)
    Assert.assert_status_code(response, status)


@pytest.mark.gectaro
@pytest.mark.smoke
def test_delete_resource_requests_id(get_config, get_id_project,
    get_project_tasks_resource_id, get_resource):
    url = get_config.get('gectaro').get('url')
    token = get_config.get('gectaro').get('token')
    id = [obj['id'] for obj in get_resource if obj['is_over_budget'] is True][0]
    response = Gectaro.delete_resource_requests_id(url, token, get_id_project, id)
    Assert.assert_status_code(response, 204)


@pytest.mark.parametrize(
    'company_id,status',
    [
        (randint(1,1000), 200) for i in range(10)
    ]
)
@pytest.mark.gectaro
@pytest.mark.smoke
def test_get_companies_resource_requests(get_config, company_id, status):
    url = get_config.get('gectaro').get('url')
    token = get_config.get('gectaro').get('token')
    response = Gectaro.get_companies_resource_requests(url, token, company_id)
    Assert.assert_status_code(response, status)
