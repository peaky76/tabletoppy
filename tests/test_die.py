from tabletoppy import Die


def test_initialize_die_with_default_correctly_sets_sides():
    die = Die()
    assert 6 == die.sides


def test_initialize_die_with_default_correctly_sets_face():
    die = Die()
    assert 1 <= die.face <= 6


def test_initialize_die_with_sides_correctly_sets_sides():
    die = Die(8)
    assert 8 == die.sides


def test_initialize_die_with_sides_correctly_sets_face():
    die = Die(8)
    assert 1 <= die.face <= 8


def test_initialize_die_with_face_correctly_sets_sides():
    die = Die(face=6)
    assert 6 == die.sides


def test_initialize_die_with_face_correctly_sets_face():
    die = Die(face=6)
    assert 6 == die.face


def test_roll_randomly_determines_a_face_to_display(mocker):
    mock_randomiser = mocker.patch("tabletoppy.die.Die._randomiser")
    mock_randomiser.return_value = 1
    die = Die()
    die.roll()
    mock_randomiser.assert_called()
