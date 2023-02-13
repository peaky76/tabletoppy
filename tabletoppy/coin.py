from enum import Enum
import random
from typing import Optional


class Coin:
    """
    A class used to represent a coin with two sides, heads and tails

    ...

    Attributes
    ----------
    face : Face
        The face of the coin currently displayed to the world
    """

    class Face(Enum):
        """
        An Enum class representing the two sides of a coin
        """

        HEADS = 1
        TAILS = 2

    def __init__(self, face: Optional[Face] = None):
        """
        Parameters
        ----------
        face : Face, optional
            The face currently displayed to the world (default will call setter which selects heads or tails at random)
        """
        self.face = face

    @property
    def face(self) -> Face:
        """
        Getter for the face attribute
        """
        return self._face

    @face.setter
    def face(self, value: Optional[Face] = None) -> None:
        """
        Setter for the face attribute

        Parameters
        ----------
        face : Face, optional
            The face currently displayed to the world (default of None will set heads or tails at random)
        """
        self._face = value or Coin.Face(random.randint(1, 2))
