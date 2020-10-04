from abc import abstractmethod
from typing import TypeVar, Protocol, Mapping, Generator

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
    def __visit_str__(self, s: str) -> VisitorResult:
        ...

    _T = TypeVar('_T')

    @abstractmethod
    def __visit_seq__(self, seq: Generator[_T, None, None]) -> VisitorResult:
        ...

    _K = TypeVar('_K')
    _V = TypeVar('_V')

    @abstractmethod
    def __visit_map__(self, map: Mapping[_K, _V]) -> VisitorResult:
        ...

    @abstractmethod
    def __visit_none__(self) -> VisitorResult:
        ...
