from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Type, TYPE_CHECKING

if TYPE_CHECKING:
    from .subject import Subject


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Type[Subject]) -> None:
        """
        Receive update from subject.
        """
        pass
