from abc import abstractmethod
from typing import Protocol
from .visitor import Visitor, VisitorResult


class Deserializer(Protocol):
    @abstractmethod
    def __deserialize_bool__(self, visitor: Visitor) -> VisitorResult:
        ...

    @abstractmethod
    def __deserialize_int__(self, visitor: Visitor) -> VisitorResult:
        ...

    @abstractmethod
    def __deserialize_float__(self, visitor: Visitor) -> VisitorResult:
        ...

    @abstractmethod
    def __deserialize_seq__(self, visitor: Visitor) -> VisitorResult:
        ...

    @abstractmethod
    def __deserialize_map__(self, visitor: Visitor) -> VisitorResult:
        ...

    @abstractmethod
    def __deserialize_none__(self, visitor: Visitor) -> VisitorResult:
        ...
