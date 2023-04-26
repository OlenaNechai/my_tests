import pytest

from homework_17.data_objects.elixir_data import ElixirData
from homework_17.data_objects.house_data import HouseData
from homework_17.data_objects.spell_data import SpellData


@pytest.fixture()
def house_mock():
    return HouseData("Gryffindor", "Godric Gryffindor", "Lion", "Fire", "Nearly-Headless Nick")


@pytest.fixture()
def elixir_mock():
    return ElixirData()


@pytest.fixture()
def spell_mock():
    return SpellData()
