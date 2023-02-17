from enum import Enum
from typing import Self

from tabletoppy.randomisable import Randomisable


class Coin(Randomisable):
    """A class used to represent a coin with two sides, heads and tails"""

    Face = Enum("Face", ["HEADS", "TAILS"])
    """An Enum representing the two sides of a coin"""

    def __init__(self, face: Face | None = None):
        """Initializer for a coin object

        :param face: The face currently displayed to the world, defaults to None, which will result in heads or tails being set at random
        :type face: Optional[Face], optional
        """
        super().__init__(Coin.Face, face)

    @property
    def face(self) -> Face:
        """The face currently displayed to the world

        :return: The face currently displayed to the world
        :rtype: Face
        """
        return self._selection

    def is_heads(self) -> bool:
        """Convenience method for checking whether the coin is showing heads

        :return: True if coin is showing heads, false otherwise
        :rtype: bool
        """
        return self.face == Coin.Face.HEADS

    def is_tails(self) -> bool:
        """Convenience method for checking whether the coin is showing tails

        :return: True if coin is showing tails, false otherwise
        :rtype: bool
        """
        return self.face == Coin.Face.TAILS

    def toss(self) -> Self:
        """Toss the coin to randomly generate a heads or tails result

        :return: The same coin with either heads or tails showing, determined randomly
        :rtype: Self
        """
        self._reset()
        return self

    def turn(self) -> Self:
        """Turns a coin to reveal the other face

        :return: The turned coin with the other face on display
        :rtype: Self
        """
        if self._selection == Coin.Face.HEADS:
            self._selection = Coin.Face.TAILS
        else:
            self._selection = Coin.Face.HEADS
        return self
