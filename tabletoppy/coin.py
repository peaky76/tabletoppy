from enum import Enum
import random
from typing import Optional, Self


class Coin:
    """A class used to represent a coin with two sides, heads and tails"""

    class Face(Enum):
        """An Enum class representing the two sides of a coin"""

        HEADS = 1
        TAILS = 2

    def __init__(self, face: Optional[Face] = None):
        """Initializer for a coin object

        :param face: The face currently displayed to the world, defaults to None, which will result in heads or tails being set at random
        :type face: Optional[Face], optional
        """
        self.face = face

    def __str__(self):
        pass

    @property
    def face(self) -> Face:
        """Getter for the face attribute

        :return: The face currently displayed to the world
        :rtype: Face
        """
        return self._face

    @face.setter
    def face(self, value: Optional[Face] = None) -> None:
        """Setter for the face attribute

        :param value: The face currently displayed to the world, defaults to None, which will result in heads or tails being set at random
        :type value: Optional[Face], optional
        """
        self._face = value or Coin.Face(random.randint(1, 2))

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
