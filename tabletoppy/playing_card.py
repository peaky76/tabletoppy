from enum import Enum
from typing import TypeVar


_E = TypeVar("_E", bound=Enum)


class PlayingCard:
    """A class used to represent a playing card

    :raises TypeError: If a joker is initialised with a suit
    :raises TypeError: If a non-joker playing card is initialised without a suit
    :return: A playing card
    :rtype: PlayingCard
    """

    class Value(Enum):
        """An Enum representing the values of a playing card"""

        JOKER = 0
        ACE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7
        EIGHT = 8
        NINE = 9
        TEN = 10
        JACK = 11
        QUEEN = 12
        KING = 13

        def __str__(self):
            return str(self.value) if 2 <= self.value <= 10 else self.name[0]

    def __init__(self, value: int | str, suit: _E | None = None):
        """Initializer for a playing card object

        :param value: The value of the playing card, can be either an int or a str
        :type value: int or str
        :param suit: The suit of the playing card, defaults to None
        :type suit: Optional[_E], optional
        """
        self.value = value
        self.suit = suit

    def __str__(self) -> str:
        """String representation of a playing card

        :return: The string representation of a playing card
        :rtype: str
        """
        if self.value is PlayingCard.Value.JOKER:
            return "Joker"
        return str(self.value) + str(self.suit)

    @property
    def suit(self) -> _E:
        """Getter for the suit of the playing card

        :return: The suit of the playing card
        :rtype: _E
        """
        return self._suit

    @suit.setter
    def suit(self, suit: _E | None) -> None:
        """Setter for the suit of the playing card"""
        if self.value is PlayingCard.Value.JOKER and suit is not None:
            raise TypeError("Joker cannot have a suit")
        if self.value is not PlayingCard.Value.JOKER and suit is None:
            raise TypeError("Playing card must have a suit")
        self._suit = suit

    @property
    def value(self) -> Value:
        """Getter for the value of the playing card

        :return: The value of the playing card
        :rtype: Value
        """
        return self._value

    @value.setter
    def value(self, value: Value) -> None:
        """Setter for the value of the playing card"""
        if isinstance(value, int):
            self._value = PlayingCard.Value(value)
        else:
            self._value = PlayingCard.Value[value.upper()]
