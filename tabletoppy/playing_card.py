from .rank import Rank
from .suit import Suit


class PlayingCard:
    """A class used to represent a playing card

    :raises TypeError: If a joker is initialised with a suit
    :raises TypeError: If a non-joker playing card is initialised without a suit
    :return: A playing card
    :rtype: PlayingCard
    """

    def __init__(self, rank: int | str, suit: Suit | None = None):
        """Initializer for a playing card object

        :param rank: The rank of the playing card, can be either an int or a str
        :type rank: int or str
        :param suit: The suit of the playing card, defaults to None
        :type suit: Optional[Suit], optional
        """
        self.rank = rank  # type: ignore
        self.suit = suit  # type: ignore

    def __str__(self) -> str:
        """String representation of a playing card

        :return: The string representation of a playing card
        :rtype: str
        """
        if self.rank is Rank.JOKER:
            return "Joker"
        return str(self.rank) + str(self.suit)

    @property
    def suit(self) -> Suit | None:
        """Getter for the suit of the playing card

        :return: The suit of the playing card
        :rtype: Suit
        """
        return self._suit

    @suit.setter
    def suit(self, suit: Suit | None) -> None:
        """Setter for the suit of the playing card"""
        if self.rank is Rank.JOKER and suit is not None:
            raise TypeError("Joker cannot have a suit")
        if self.rank is not Rank.JOKER and suit is None:
            raise TypeError("Playing card must have a suit")
        self._suit: Suit | None = suit

    @property
    def rank(self) -> Rank:
        """Getter for the rank of the playing card

        :return: The rank of the playing card
        :rtype: Value
        """
        return self._rank

    @rank.setter
    def rank(self, rank: int | str) -> None:
        """Setter for the rank of the playing card"""
        if isinstance(rank, int):
            self._rank = Rank(rank)
        else:
            self._rank = Rank[rank.upper()]
