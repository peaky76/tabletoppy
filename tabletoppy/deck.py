from .playing_card import playing_card


class Deck:
    def __init__(self):
        """Initializer for a deck object"""
        self.cards = [
            playing_card(value, suit)
            for value in PlayingCard.Value
            for suit in PlayingCard.Suit
        ]
