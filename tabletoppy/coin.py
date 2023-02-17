from enum import Enum
import random
from typing import Self


class Coin:
    """A class used to represent a coin with two sides, heads and tails"""

    Face = Enum("Face", ["HEADS", "TAILS"])
    """An Enum representing the two sides of a coin"""

    def __init__(self, face: Face | None = None):
        """Initializer for a coin object

        :param face: The face currently displayed to the world, defaults to None, which will result in heads or tails being set at random
        :type face: Optional[Face], optional
        """
        self.face = face

    def __str__(self):
        return f"Coin showing {self.face.name}"

    @property
    def face(self) -> Face:  # type: ignore
        """Getter for the face attribute

        :return: The face currently displayed to the world
        :rtype: Face
        """
        return self._face

    @face.setter
    def face(self, value: Face | None = None) -> None:
        """Setter for the face attribute

        :param value: The face currently displayed to the world, defaults to None, which will result in heads or tails being set at random
        :type value: Optional[Face], optional
        """
        self._face = value or Coin.Face(random.randint(1, 2))

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
        self.face = None
        return self

    def turn(self) -> Self:
        """Turns a coin to reveal the other face

        :return: The turned coin with the other face on display
        :rtype: Self
        """
        if self.face == Coin.Face.HEADS:
            self.face = Coin.Face.TAILS
        else:
            self.face = Coin.Face.HEADS
        return self
