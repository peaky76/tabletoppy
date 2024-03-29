import pytest

from tabletoppy import Suit
from tabletoppy.playing_card import PlayingCard


def test_playing_card_can_be_initialised_with_int_value_and_suit():
    assert PlayingCard(3, Suit.HEARTS)


def test_playing_card_can_be_initialised_with_str_value_and_suit():
    assert PlayingCard("Ace", Suit.HEARTS)


def test_playing_card_can_be_initialised_with_alt_str_value_and_suit():
    assert PlayingCard("Deuce", Suit.HEARTS)


def test_playing_card_can_be_initialised_with_joker_and_no_suit():
    assert PlayingCard("Joker")


def test_playing_card_cannot_be_initialised_with_any_other_value_without_suit():
    with pytest.raises(TypeError):
        assert PlayingCard("Ace")


def test_playing_card_string_representation_for_numerals():
    assert str(PlayingCard(10, Suit.SPADES)) == "10♠"


def test_playing_card_string_representation_for_special_cards():
    assert str(PlayingCard("Ace", Suit.SPADES)) == "A♠"


def test_playing_card_string_representation_for_joker():
    assert str(PlayingCard("Joker")) == "Joker"
