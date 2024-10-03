import json

from core.request import Request


class Gectaro:
    @staticmethod
    def get_companies(url:str, token:str):
        headers = {"Authorization": f"Bearer {token}"}
        endpoint = 'companies'
        response = Request.get(f'{url}{endpoint}',headers=headers)
        return response

    @staticmethod
    def get_projects(url:str, token:str, company_id:int):
        headers = {"Authorization": f"Bearer {token}"}
        endpoint = f'companies/{company_id}/projects'
        response = Request.get(f'{url}{endpoint}', headers=headers)
        return response

    @staticmethod
    def post_projects(url:str, token:str, company_id:int, data:dict):
        headers = {"Authorization": f"Bearer {token}",'accept': '*/*'}
        endpoint = f'companies/{company_id}/projects'
        files = {
            'name': (None, data['name']),
            'status': (None, data['status']),
        }
        response = Request.post(f'{url}{endpoint}', headers=headers, files=files)
        return response

    @staticmethod
    def post_resource_requests(url:str, token:str, project_id:int, data:dict):
        headers = {"Authorization": f"Bearer {token}", 'accept': '*/*'}
        endpoint = f'projects/{project_id}/resource-requests'
        files = {key: (None, value) for key, value in data.items() }
        response = Request.post(f'{url}{endpoint}', headers=headers, files=files)
        return response


    @staticmethod
    def get_resource_requests(url:str, token:str, project_id:int):
        headers = {"Authorization": f"Bearer {token}"}
        endpoint = f'projects/{project_id}/resource-requests'
        response = Request.get(f'{url}{endpoint}', headers=headers)
        return response

    @staticmethod
    def get_companies_resource_requests(url, token, company_id):
        headers = {"Authorization": f"Bearer {token}"}
        endpoint = f'companies/{company_id}/resource-requests'
        response = Request.get(f'{url}{endpoint}', headers=headers)
        return response

    @staticmethod
    def get_resource_requests_id(url:str, token:str, project_id:int, id:int):
        headers = {"Authorization": f"Bearer {token}"}
        endpoint = f'projects/{project_id}/resource-requests/{id}'
        response = Request.get(f'{url}{endpoint}', headers=headers)
        return response

    @staticmethod
    def put_resource_requests_id(url:str, token:str, project_id:int, id:int, data:dict):
        headers = {"Authorization": f"Bearer {token}"}
        endpoint = f'projects/{project_id}/resource-requests/{id}'
        files = {
            'project_tasks_resource_id': (None, data['project_tasks_resource_id']),
            'volume': (None, data['volume']),
            'cost': (None, data['cost']),
            'is_over_budget': (None, data['is_over_budget']),
        }
        response = Request.put(f'{url}{endpoint}', headers=headers,files=files)
        return response

    @staticmethod
    def delete_resource_requests_id(url: str, token: str, project_id: int, id: int):
        headers = {"Authorization": f"Bearer {token}"}
        endpoint = f'projects/{project_id}/resource-requests/{id}'
        response = Request.delete(f'{url}{endpoint}', headers=headers)
        return response