from homework_17.utilities.api.base_api import BaseAPI


class SpellsAPI(BaseAPI):
    def __init__(self, env):
        super().__init__(env)
        self.__spells_url = '/Spells'

    def get_spell(self, spell_id, headers=None):
        response = self.get(url=f'{self.__spells_url}/{spell_id}', headers=headers)
        return response
