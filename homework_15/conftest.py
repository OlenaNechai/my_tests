import pytest

from homework_15.human import Human


@pytest.fixture()
def create_human_with_params():
    def __create_human(name: str, age: int, gender: str):
        return Human(name, age, gender)

    yield __create_human


@pytest.fixture()
def create_dead_human():
    return Human('Mike', 100, 'male')
