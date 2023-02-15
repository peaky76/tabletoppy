from typing import Optional


class Die:
    def __init__(self, sides: Optional[int] = 6):
        """Initializer for a die object

        :param sides: The number of sides on the die, defaults to 6
        :type sides: Optional[int], optional
        """
        self.sides = sides
