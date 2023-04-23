from enum import Enum


class Rank(Enum):
    """An Enum representing the ranks of a playing card"""

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

    # Alternative names for the values
    DEUCE = TWO
    TREY = THREE

    def __str__(self):
        if self.value == 0:
            return "Joker"
        return str(self.value) if 2 <= self.value <= 10 else self.name[0]
