import pytest


@pytest.mark.parametrize('age', [30, 99])
def test_grow(create_human_with_params, age):
    human = create_human_with_params('Mike', age, 'male')
    human.grow()
    assert human.age == age + 1, "Human age is updated incorrectly"


def test_change_gender(create_human_with_params):
    human = create_human_with_params('Mike', 30, 'male')
    human.change_gender('female')
    assert human.gender == 'female', "Gender was not changed"


def test_dead_can_grow_exception(create_dead_human):
    dead_human = create_dead_human
    with pytest.raises(Exception) as exception_info:
        dead_human.grow()

    assert str(exception_info.value) == f"{dead_human.name} is already dead..."


def test_change_gender_to_same_exception(create_human_with_params):
    human = create_human_with_params('Mike', 30, 'male')
    with pytest.raises(Exception) as exception_info:
        human.change_gender('male')

    assert str(exception_info.value) == f"{human.name} already has gender '{human.gender}'"


def test_change_gender_to_incorrect_exception(create_human_with_params):
    human = create_human_with_params('Mike', 30, 'male')
    with pytest.raises(Exception) as exception_info:
        human.change_gender('unknown')

    assert str(exception_info.value) == "Not correct name of gender"
