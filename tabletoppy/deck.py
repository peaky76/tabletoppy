from .playing_card import PlayingCard
from .suit import Suit


class Deck:
    def __init__(self):
        """Initializer for a deck object"""
        self.cards = [
            PlayingCard(value.value, suit)
            for value in PlayingCard.Value
            for suit in Suit
            if value is not PlayingCard.Value.JOKER
        ]
