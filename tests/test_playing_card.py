from tabletoppy.playing_card import PlayingCard
from tabletoppy import Suit


def test_playing_card_can_be_initialised_with_int_value_and_suit():
    assert PlayingCard(3, Suit.HEARTS)


def test_playing_card_can_be_initialised_with_str_value_and_suit():
    assert PlayingCard("Ace", Suit.HEARTS)
