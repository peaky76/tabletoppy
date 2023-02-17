from enum import Enum
from typing import Self

from tabletoppy.randomisable import Randomisable


class Die(Randomisable):
    def __init__(self, sides: int = 6, face: int | None = None):
        """Initializer for a die object

        :param sides: The number of sides on the die, defaults to 6
        :type sides: Optional[int], optional
        """
        self.sides = sides
        Face = Enum("Face", [str(x + 1) for x in range(sides)])
        super().__init__(Face, Face(face) if face else None)

    @property
    def face(self) -> int:
        """Getter for the face attribute

        :return: The current uppermost face of the die
        :rtype: int
        """
        return int(self._selection.name)

    def roll(self) -> Self:
        """Roll the die to randomly generate a number matching one of the sides

        :return: The die with a randomly determined face lying uppermost
        :rtype: Self
        """
        self._reset()
        return self
