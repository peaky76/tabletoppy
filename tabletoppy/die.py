import random
from typing import Optional, Self


class Die:
    def __init__(self, sides: Optional[int] = 6):
        """Initializer for a die object

        :param sides: The number of sides on the die, defaults to 6
        :type sides: Optional[int], optional
        """
        self.sides = sides
        self.face = None

    @property
    def face(self) -> int:
        """Getter for the face attribute

        :return: The current uppermost face of the die
        :rtype: int
        """
        return self._face

    @face.setter
    def face(self, value: Optional[int] = None) -> None:
        """Setter for the face attribute

        :param value: The current uppermost face of the die, defaults to None, which will set it randomly
        :type value: Optional[int], optional
        """
        self._face = value or random.randint(1, self.sides)

    def roll(self) -> Self:
        """Roll the die to randomly generate a number matching one of the sides

        :return: The die with a randomly determined face lying uppermost
        :rtype: Self
        """
        self.face = None
        return self
