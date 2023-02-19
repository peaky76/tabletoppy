from enum import Enum


class Suit(Enum):
    SPADES = "\u2660"
    HEARTS = "\u2665"
    CLUBS = "\u2663"
    DIAMONDS = "\u2666"

    def __new__(cls, *args, **kwds):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, unicode: str):
        self._unicode_ = unicode

    def __str__(self):
        return self.name

    @property
    def unicode(self):
        return self._unicode_
