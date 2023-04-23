from .playing_card import PlayingCard
from .suit import Suit


class Deck:
    def __init__(self, jokers: int = 0):
        """Initializer for a deck object"""
        self.cards = [
            PlayingCard(value, suit) for value in range(1, 14) for suit in Suit
        ]
        if jokers:
            self.cards.extend([PlayingCard("Joker")] * jokers)
