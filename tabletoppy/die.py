import random
from typing import Self


class Die:
    def __init__(self, sides: int = 6, face: int | None = None):
        """Initializer for a die object

        :param sides: The number of sides on the die, defaults to 6
        :type sides: Optional[int], optional
        """
        self.sides = sides
        self.face = face

    def get_face(self) -> int:  # type: ignore
        """Getter for the face attribute

        :return: The current uppermost face of the die
        :rtype: int
        """
        return self._face

    def set_face(self, value: int | None = None) -> None:
        """Setter for the face attribute

        :param value: The current uppermost face of the die, defaults to None, which will set it randomly
        :type value: Optional[int], optional
        """
        self._face = value or random.randint(1, self.sides)

    face = property(get_face, set_face)

    def roll(self) -> Self:
        """Roll the die to randomly generate a number matching one of the sides

        :return: The die with a randomly determined face lying uppermost
        :rtype: Self
        """
        self.face = None
        return self
