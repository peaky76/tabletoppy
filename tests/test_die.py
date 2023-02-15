from tabletoppy import Die


def test_initialize_die_with_default():
    die = Die()
    assert 6 == die.sides


def test_initialize_die_with_sides():
    die = Die(8)
    assert 8 == die.sides
