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
        self.options = options
        self.selection = selection

    def get_selection(self) -> _E:  # type: ignore
        """Getter for the current selection

        :return: The currently selected option
        :rtype: Enum
        """
        return self._selection

    def set_selection(self, value: _E | None = None) -> None:
        """Setter for the current selection

        :param value: The option which will become the new selection, defaults to None at which point an option will be selected at random
        :type value: Optional[Enum], optional
        :raises TypeError: if a suitable option has not been given
        """
        if value and not isinstance(value, Enum):
            raise TypeError(f"{value} is not an instance of {self.options}")
        self._selection = value or self.options(self._randomiser())

    selection = property(get_selection, set_selection)

    def _randomiser(self) -> int:
        """Private function to generate a integer corresponding to one of the options

        :return: An integer corresponding to a value in the options
        :rtype: int
        """
        return random.randint(1, len(self.options))

    def _reset(self) -> None:
        """Private function to set selection to None, thereby prompting it to be randomised"""
        self.selection = None