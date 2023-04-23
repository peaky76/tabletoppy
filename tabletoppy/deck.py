from collections import deque
from .playing_card import PlayingCard as Card
from .suit import Suit


class Deck:
    def __init__(self, *, jokers: int = 0, packs: int = 1):
        """Initializes a standard deck of playing cards, default is a standard 52 card deck

        :param jokers: The number of jokers to add to the deck, defaults to 0
        :type jokers: int, optional
        :param packs: The number of packs to add to the deck, defaults to 1
        :type packs: int, optional
        """
        regular_cards = [Card(n, suit) for n in range(1, 14) for suit in Suit] * packs
        added_cards = [Card("Joker")] * jokers
        self.cards = deque(regular_cards + added_cards)

    def cut(self):
        pass

    def draw(self) -> Card:
        """Draws the top card from the deck

        :return: The top card from the deck
        :rtype: PlayingCard
        """
        return self.cards.pop()

    def shuffle(self):
        pass

    def sort(self):
        pass
