from tabletoppy import Coin


def test_initialize_coin_with_heads():
    face = Coin.Face.HEADS
    coin = Coin(face)
    assert face == coin.face


def test_initialize_coin_with_tails():
    face = Coin.Face.TAILS
    coin = Coin(face)
    assert face == coin.face


def test_initialize_coin_with_no_args_produces_either_heads_or_tails():
    coin = Coin()
    assert coin.face in [Coin.Face.HEADS, Coin.Face.TAILS]
