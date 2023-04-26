from http import HTTPStatus

from homework_17.api_collections.elixirs_api import ElixirsAPI
from homework_17.api_collections.houses_api import HousesAPI
from homework_17.api_collections.spells_api import SpellsAPI
from homework_17.data_objects.elixir_data import ElixirData
from homework_17.data_objects.house_data import HouseData
from homework_17.data_objects.spell_data import SpellData


def test_get_house_by_id(env, house_mock):
    expected_house = house_mock
    response = HousesAPI(env).get_hogwarts_house("0367baf3-1cb6-4baf-bede-48e17e1cd005")
    response_data = response.json()
    actual_house = HouseData.from_json(**response_data)
    assert response.status_code == HTTPStatus.OK, 'Status code is not as expected'
    assert actual_house == expected_house, 'House data is not as expected'


def test_get_elixir_by_id(env, elixir_mock):
    expected_elixir = elixir_mock
    response = ElixirsAPI(env).get_elixir("7f435277-1149-4a07-8316-82a02c77d4ee")
    response_data = response.json()
    actual_elixir = ElixirData.from_json(**response_data)
    assert response.status_code == HTTPStatus.OK, 'Status code is not as expected'
    assert actual_elixir == expected_elixir, 'Elixir data is not as expected'


def test_get_spell_by_id(env, spell_mock):
    expected_spell = spell_mock
    response = SpellsAPI(env).get_spell("aede8168-528c-4888-8c14-a38b6c5e6a97")
    response_data = response.json()
    actual_spell = SpellData.from_json(**response_data)
    assert response.status_code == HTTPStatus.OK, 'Status code is not as expected'
    assert actual_spell == expected_spell, 'Spell data is not as expected'
