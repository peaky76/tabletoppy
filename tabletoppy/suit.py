from enum import Enum


class Suit(Enum):
    """An enumeration of the four suits of a standard deck of playing cards

    :param Enum: An Enum representing the four suits of a standard deck of playing cards
    :type Enum: Enum
    :return: A new instance of the Suit Enum
    :rtype: Enum
    """

    SPADES = "\u2660"
    HEARTS = "\u2665"
    CLUBS = "\u2663"
    DIAMONDS = "\u2666"

    def __new__(cls, *args, **kwargs):
        """A custom __new__ method to ensure that the value of each member is the next integer in the sequence

        :return: A new instance of the Suit Enum
        :rtype: Enum
        """
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, unicode: str):
        """A custom __init__ method to ensure that each member gets set with a unicode value

        :param unicode: The unicode value to be assigned to the member
        :type unicode: str
        """
        self._unicode_ = unicode

    def __str__(self):
        """A custom __str__ method to ensure that the unicode value is returned when the member is converted to a string

        :return: The unicode value of the member
        :rtype: str
        """
        return self._unicode_
