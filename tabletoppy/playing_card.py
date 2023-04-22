from enum import Enum
from typing import TypeVar


_E = TypeVar("_E", bound=Enum)


class PlayingCard:
    class Value(Enum):
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

    def __init__(self, value: int | str, suit: _E):
        self.value = (
            PlayingCard.Value(value)
            if isinstance(value, int)
            else PlayingCard.Value[value.upper()]
        )
        self.suit = suit
