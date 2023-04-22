from enum import Enum
from typing import TypeVar


_E = TypeVar("_E", bound=Enum)


class PlayingCard:
    class Value(Enum):
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

    def __init__(self, value: int | str, suit: _E | None = None):
        self.value = value
        self.suit = suit

    @property
    def suit(self) -> _E:
        return self._suit

    @suit.setter
    def suit(self, suit: _E | None) -> None:
        if self.value is PlayingCard.Value.JOKER and suit is not None:
            raise TypeError("Joker cannot have a suit")
        if self.value is not PlayingCard.Value.JOKER and suit is None:
            raise TypeError("Playing card must have a suit")
        self._suit = suit

    @property
    def value(self) -> Value:
        return self._value

    @value.setter
    def value(self, value: Value) -> None:
        if isinstance(value, int):
            self._value = PlayingCard.Value(value)
        else:
            self._value = PlayingCard.Value[value.upper()]
