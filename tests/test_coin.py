import random
from tabletoppy import Coin


[HEADS, TAILS] = Coin.Face


def test_initialize_coin_with_heads():
    coin = Coin(HEADS)
    assert HEADS == coin.face


def test_initialize_coin_with_tails():
    coin = Coin(TAILS)
    assert TAILS == coin.face


def test_initialize_coin_default_produces_either_heads_or_tails():
    coin = Coin()
    assert coin.face in [HEADS, TAILS]


def test_str_representation_of_coin_is_as_intended():
    coin = Coin(HEADS)
    expected = "Coin showing HEADS"
    assert expected == str(coin)


def test_is_heads_returns_true_when_coin_face_is_heads():
    coin = Coin(HEADS)
    assert coin.is_heads()


def test_is_heads_returns_false_when_coin_face_is_heads():
    coin = Coin(TAILS)
    assert not coin.is_heads()


def test_is_tails_returns_true_when_coin_face_is_heads():
    coin = Coin(TAILS)
    assert coin.is_tails()


def test_is_tails_returns_false_when_coin_face_is_heads():
    coin = Coin(HEADS)
    assert not coin.is_tails()


def test_toss_randomly_determines_heads_or_tails(mocker):
    mock_randomiser = mocker.patch("tabletoppy.coin.Coin._randomiser")
    mock_randomiser.return_value = 1
    coin = Coin()
    coin.toss()
    mock_randomiser.assert_called()


def test_turn_coin_displaying_heads_puts_tails_on_display():
    coin = Coin(HEADS)
    coin.turn()
    assert TAILS == coin.face


def test_turn_coin_displaying_tails_puts_heads_on_display():
    coin = Coin(TAILS)
    coin.turn()
    assert HEADS == coin.face
