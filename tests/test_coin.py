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


def test_initialize_coin_default_randomly_determines_heads_or_tails(mocker):
    mock_random = mocker.patch("tabletoppy.coin.random")
    mocker.patch("tabletoppy.coin.Coin.Face")
    Coin()
    mock_random.randint.assert_called_with(1, 2)


def test_initialize_coin_default_sets_heads_or_tails_as_randomly_generated(mocker):
    mock_random = mocker.patch("tabletoppy.coin.random")
    mock_random.randint.return_value = 1
    coin = Coin()
    assert HEADS == coin.face


def test_turn_coin_displaying_heads_puts_tails_on_display():
    coin = Coin(HEADS)
    coin.turn()
    assert TAILS == coin.face


def test_turn_coin_displaying_tails_puts_heads_on_display():
    coin = Coin(TAILS)
    coin.turn()
    assert HEADS == coin.face
