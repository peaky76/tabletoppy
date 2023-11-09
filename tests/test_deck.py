import pytest

from tabletoppy.deck import Deck


def test_deck_init_without_jokers_creates_52_cards():
    deck = Deck()
    assert len(deck.cards) == 52


def test_deck_init_with_jokers_creates_54_cards():
    deck = Deck(jokers=2)
    assert len(deck.cards) == 54


def test_deck_with_multiple_packs_of_cards():
    deck = Deck(packs=2)
    assert len(deck.cards) == 104


def test_deck_first_card_is_ace_of_spades_in_standard_deck_with_standard_order():
    deck = Deck()
    assert str(deck.cards.popleft()) == "A♠"


def test_deck_last_card_is_king_of_diamonds_in_standard_deck_with_standard_order():
    deck = Deck()
    assert str(deck.cards.pop()) == "K♦"


def test_deck_last_card_is_joker_in_standard_deck_with_jokers_and_standard_order():
    deck = Deck(jokers=2)
    assert str(deck.cards.pop()) == "Joker"


def test_deck_size_property():
    deck = Deck()
    assert deck.size == 52


def test_deck_add_to_bottom_card_goes_to_front_of_deque():
    deck = Deck()
    deck.add_to_bottom("6♠")
    assert str(deck.cards.popleft()) == "6♠"


def test_deck_add_to_top_card_goes_to_end_of_deque():
    deck = Deck()
    deck.add_to_top("6♠")
    assert str(deck.cards.pop()) == "6♠"


def test_deck_cut_returns_the_cut_card(mocker):
    deck = Deck()
    mocker.patch("tabletoppy.deck.randint", return_value=26)
    assert str(deck.cut()) == "A♣"


def test_deck_cut_applies_minimum_depth():
    deck = Deck()
    cut_card = deck.cut(min_depth=26)
    assert str(cut_card) == "A♣"


def test_deck_cut_raises_value_error_if_minimum_depth_below_range():
    deck = Deck()
    with pytest.raises(ValueError):
        deck.cut(min_depth=0)


def test_deck_cut_raises_value_error_if_minimum_depth_above_range():
    deck = Deck()
    with pytest.raises(ValueError):
        deck.cut(min_depth=30)


def test_deck_cut_alters_order_of_deck():
    deck = Deck()
    deck.cut(min_depth=2)
    assert str(deck.cards.popleft()) != "A♠"
    assert str(deck.cards.pop()) != "K♦"


def test_deck_deal_returns_hand_of_cards():
    deck = Deck()
    hand = deck.deal(5)
    assert hand.size == 5


def test_deck_deal_returns_top_cards_in_deck_as_new_deck():
    deck = Deck()
    hand = deck.deal(5)
    assert ["K♦", "Q♦", "J♦", "10♦", "9♦"] == [str(card) for card in hand.cards]


def test_deck_draw_returns_top_card_in_deck():
    deck = Deck()
    assert str(deck.draw()) == "K♦"


def test_deck_shuffle_returns_shuffled_deck():
    deck = Deck()
    deck.shuffle()
    assert str(deck.cards.popleft()) != "A♠"
    assert str(deck.cards.pop()) != "K♦"
