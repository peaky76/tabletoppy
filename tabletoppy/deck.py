from collections import deque
from .playing_card import PlayingCard as Card
from .suit import Suit


class Deck:
    def __init__(self, jokers: int = 0):
        """Initializes a standard deck of playing cards, default is a standard 52 card deck

        param jokers: The number of jokers to add to the deck, defaults to 0
        type jokers: int, optional
        """
        regular_cards = [Card(val, suit) for val in range(1, 14) for suit in Suit]
        added_cards = [Card("Joker")] * jokers
        self.cards = deque(regular_cards + added_cards)

    def cut(self):
        pass

    def draw(self):
        pass

    def shuffle(self):
        pass

    def sort(self):
        pass
