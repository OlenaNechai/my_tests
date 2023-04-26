from homework_17.utilities.api.base_api import BaseAPI


class ElixirsAPI(BaseAPI):
    def __init__(self, env):
        super().__init__(env)
        self.__elixirs_url = '/Elixirs'

    def get_elixir(self, elixir_id, headers=None):
        response = self.get(url=f'{self.__elixirs_url}/{elixir_id}', headers=headers)
        return response
