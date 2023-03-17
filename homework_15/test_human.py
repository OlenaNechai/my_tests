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


def test_grow_exception(create_dead_human):
    human = create_dead_human
    human.grow()
    with pytest.raises(Exception):
        human.grow()


def test_change_gender_to_same_exception(create_human_with_params):
    human = create_human_with_params('Mike', 30, 'male')
    with pytest.raises(Exception):
        human.change_gender('male')


def test_change_gender_to_incorrect_exception(create_human_with_params):
    human = create_human_with_params('Mike', 30, 'male')
    with pytest.raises(Exception):
        human.change_gender('unknown')
