from abc import abstractmethod
from typing import TypeVar, Protocol

VisitorResult = TypeVar("VisitorResult")


class Visitor(Protocol):
    @abstractmethod
    def __visit_bool__(self, visitor: bool) -> VisitorResult:
        ...

    @abstractmethod
    def __visit_int__(self, value: int) -> VisitorResult:
        ...

    @abstractmethod
    def __visit_float__(self, value: float) -> VisitorResult:
        ...

    @abstractmethod
    def __visit_list__(self) -> VisitorResult:
        ...

    @abstractmethod
    def __visit_dict__(self) -> VisitorResult:
        ...

    @abstractmethod
    def __visit_none__(self) -> VisitorResult:
        ...
