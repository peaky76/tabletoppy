from enum import Enum
import random
from typing import Optional


class Coin:
    class Face(Enum):
        HEADS = 1
        TAILS = 2

    def __init__(self, face: Optional[Face] = None):
        self.face = face

    @property
    def face(self) -> Face:
        return self._face

    @face.setter
    def face(self, value: Optional[Face] = None) -> None:
        self._face = value or Coin.Face(random.randint(1, 2))
