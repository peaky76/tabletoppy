from tabletoppy.deck import Deck


def test_deck_init_without_jokers_creates_52_cards():
    deck = Deck()
    assert 52 == len(deck.cards)


def test_deck_init_with_jokers_creates_54_cards():
    deck = Deck(jokers=2)
    assert 54 == len(deck.cards)


def test_deck_with_multiple_packs_of_cards():
    deck = Deck(packs=2)
    assert 104 == len(deck.cards)


def test_deck_first_card_is_ace_of_spades_in_standard_deck_with_standard_order():
    deck = Deck()
    assert "A♠" == str(deck.cards.popleft())


def test_deck_last_card_is_king_of_diamonds_in_standard_deck_with_standard_order():
    deck = Deck()
    assert "K♦" == str(deck.cards.pop())


def test_deck_last_card_is_joker_in_standard_deck_with_jokers_and_standard_order():
    deck = Deck(jokers=2)
    assert "Joker" == str(deck.cards.pop())


def test_deck_add_to_bottom_card_goes_to_front_of_deque():
    deck = Deck()
    deck.add_to_bottom("6♠")
    assert "6♠" == str(deck.cards.popleft())


def test_deck_add_to_top_card_goes_to_end_of_deque():
    deck = Deck()
    deck.add_to_top("6♠")
    assert "6♠" == str(deck.cards.pop())


def test_deck_draw_returns_top_card_in_deck():
    deck = Deck()
    assert "K♦" == str(deck.draw())
