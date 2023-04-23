from collections import deque
from random import randint
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

    def add_to_bottom(self, card: Card) -> None:
        """Adds a card to the bottom of the deck

        :param card: The card to add to the bottom of the deck
        :type card: PlayingCard
        """
        self.cards.appendleft(card)

    def add_to_top(self, card: Card) -> None:
        """Adds a card to the top of the deck

        :param card: The card to add to the top of the deck
        :type card: PlayingCard
        """
        self.cards.append(card)

    def cut(self, min_depth: int = 1) -> Card:
        """Cuts the deck at a random point, returns the card at that point and re-combines the cut deck

        :return: The card at the cut point
        :rtype: PlayingCard
        """
        i = randint(min_depth, (len(self.cards) - min_depth))
        self.cards = deque(list(self.cards)[i:] + list(self.cards)[:i])
        return self.cards[0]

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
