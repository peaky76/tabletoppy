from tabletoppy.deck import Deck


def test_deck_init_without_jokers_creates_52_cards():
    deck = Deck()
    assert 52 == len(deck.cards)


def test_deck_init_with_jokers_creates_54_cards():
    deck = Deck(jokers=2)
    assert 54 == len(deck.cards)
