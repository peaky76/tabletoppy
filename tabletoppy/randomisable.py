from abc import ABC
from enum import Enum
import random
from typing import Type, TypeVar

_E = TypeVar("_E", bound=Enum)


class Randomisable(ABC):
    def __init__(self, options: Type[_E], selection: _E | None = None):
        """Abstract base class for any object that can be randomised to create a selection, such as a coin (by tossing), a dice (by rolling) or a card (by drawing)

        :param options: An Enum representing the range of values from which the selection will be made
        :type options: Enum
        :param selection: The currently selected value, defaults to None, which will result in a value being selected at random
        :type selection: Optional[Enum], optional
        """
        self._options = options
        self._selection = selection

    def __str__(self):
        return f"{self.__class__.__name__} showing {self._selection.name}"

    def get__selection(self) -> _E:  # type: ignore
        """Getter for the current selection

        :return: The currently selected option
        :rtype: Enum
        """
        return self.__selection

    def set__selection(self, value: _E | None = None) -> None:
        """Setter for the current selection

        :param value: The option which will become the new selection, defaults to None at which point an option will be selected at random
        :type value: Optional[Enum], optional
        :raises TypeError: if a suitable option has not been given
        """
        if value and not isinstance(value, Enum):
            raise TypeError(f"{value} is not an instance of {self._options}")
        self.__selection = value or self._options(self._randomiser())

    _selection = property(get__selection, set__selection)

    def _randomiser(self) -> int:
        """Private function to generate a integer corresponding to one of the options

        :return: An integer corresponding to a value in the options
        :rtype: int
        """
        return random.randint(1, len(self._options))

    def _reset(self) -> None:
        """Private function to set selection to None, thereby prompting it to be randomised"""
        self._selection = None
