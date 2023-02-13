from tabletoppy import Coin


def test_initialize_coin_with_heads():
    face = Coin.Face.HEADS
    coin = Coin(face)
    assert face == coin.face


def test_initialize_coin_with_tails():
    face = Coin.Face.TAILS
    coin = Coin(face)
    assert face == coin.face


def test_initialize_coin_default_produces_either_heads_or_tails():
    coin = Coin()
    assert coin.face in [Coin.Face.HEADS, Coin.Face.TAILS]


def test_initialize_coin_default_randomly_determines_heads_or_tails(mocker):
    mock_random = mocker.patch("tabletoppy.coin.random")
    mocker.patch("tabletoppy.coin.Coin.Face")
    Coin()
    mock_random.randint.assert_called_with(1, 2)


def test_initialize_coin_default_sets_heads_or_tails_as_randomly_generated(mocker):
    mock_random = mocker.patch("tabletoppy.coin.random")
    mock_random.randint.return_value = 1
    face = Coin.Face.HEADS
    coin = Coin()
    assert face == coin.face
