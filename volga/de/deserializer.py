from abc import abstractmethod
from typing import Protocol
from .visitor import VisitorResult


class Deserializer(Protocol):
    @abstractmethod
    def __deserialize_bool__(self, visitor: bool) -> VisitorResult:
        ...

    @abstractmethod
    def __deserialize_int__(self, value: int) -> VisitorResult:
        ...

    @abstractmethod
    def __deserialize_float__(self, value: float) -> VisitorResult:
        ...

    @abstractmethod
    def __deserialize_list__(self) -> VisitorResult:
        ...

    @abstractmethod
    def __deserialize_dict__(self) -> VisitorResult:
        ...

    @abstractmethod
    def __deserialize_none__(self) -> VisitorResult:
        ...
