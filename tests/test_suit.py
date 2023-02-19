from tabletoppy.suit import Suit


def test_suit_str():
    assert "SPADES" == str(Suit.SPADES)


def test_suit_unicode():
    assert "♠" == Suit.SPADES.unicode
