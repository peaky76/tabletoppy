from enum import Enum

import pytest
from tabletoppy.randomisable import Randomisable

Foobar = Enum("Foobar", ["ALPHA", "BETA", "GAMMA"])


def test_initialize_randomisable_correctly_sets_options():
    randomisable = Randomisable(Foobar)
    assert Foobar == randomisable._options


def test_initialize_randomisable_correctly_sets_selection():
    randomisable = Randomisable(Foobar, Foobar.ALPHA)
    assert Foobar.ALPHA == randomisable.selection


def test_initialize_randomisable_with_invalid_selection_raises_type_error():
    with pytest.raises(TypeError):
        Randomisable(Foobar, 6)


def test_initialize_randomisable_determines_selection_using_randomiser(mocker):
    mock_randomiser = mocker.patch("tabletoppy.randomisable.Randomisable._randomiser")
    mock_randomiser.return_value = 1
    Randomisable(Foobar)
    mock_randomiser.assert_called()


def test_initialize_randomisable_determines_selection_as_randomly_generated(mocker):
    mock_randomiser = mocker.patch("tabletoppy.randomisable.Randomisable._randomiser")
    mock_randomiser.return_value = 2
    randomisable = Randomisable(Foobar)
    assert Foobar.BETA == randomisable.selection


def test_randomiser_generates_random_integer_with_options_as_limit(mocker):
    mock_random = mocker.patch("tabletoppy.randomisable.random")
    mock_random.randint.return_value = 1
    randomisable = Randomisable(Foobar)
    randomisable._randomiser()
    mock_random.randint.assert_called_with(1, len(randomisable._options))


def test_reset_invokes_randomiser(mocker):
    randomisable = Randomisable(Foobar)
    mock_randomiser = mocker.patch("tabletoppy.randomisable.Randomisable._randomiser")
    mock_randomiser.return_value = 1
    randomisable._reset()
    mock_randomiser.assert_called()
