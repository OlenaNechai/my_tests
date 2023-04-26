import requests


class BaseAPI:
    def __init__(self, env):
        self.__request = requests
        self.__base_url = env.base_api_url
        self.__headers = {"Accept": "text/plain"}

    def get(self, url, headers=None, params=None):
        if headers is None:
            headers = self.__headers
        response = self.__request.get(f'{self.__base_url}{url}', headers=headers, params=params)
        return response

    def post(self, url, body, headers=None, params=None):
        if headers is None:
            headers = self.__headers
        response = self.__request.post(f'{self.__base_url}{url}', data=body, headers=headers, params=params)
        return response

    def put(self):
        ...

    def patch(self):
        ...

    def delete(self):
        ...
