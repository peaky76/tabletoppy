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


def test_initialize_randomly_determines_face(mocker):
    mock_random = mocker.patch("tabletoppy.die.random")
    Die()
    mock_random.randint.assert_called_with(1, 6)


def test_initialize_uses_sides_as_randint_limit(mocker):
    mock_random = mocker.patch("tabletoppy.die.random")
    Die(8)
    mock_random.randint.assert_called_with(1, 8)


def test_initialize_sets_face_as_randomly_generated(mocker):
    mock_random = mocker.patch("tabletoppy.die.random")
    mock_random.randint.return_value = 4
    die = Die()
    assert 4 == die.face


def test_roll_randomly_determines_a_face_to_display(mocker):
    die = Die()
    mock_random = mocker.patch("tabletoppy.die.random")
    die.roll()
    mock_random.randint.assert_called_with(1, 6)
