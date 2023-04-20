from tabletoppy.suit import Suit


def test_suit_str():
    assert "♠" == str(Suit.SPADES)
