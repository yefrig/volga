from abc import abstractmethod
from typing import Protocol, TypeVar, Sequence, Mapping


class Serializer(Protocol):
    @abstractmethod
    def __serialize_bool__(self, value: bool) -> None:
        ...

    @abstractmethod
    def __serialize_int__(self, value: int) -> None:
        ...

    @abstractmethod
    def __serialize_float__(self, value: float) -> None:
        ...

    @abstractmethod
    def __serialize_str__(self, s: str) -> None:
        ...

    _T = TypeVar("_T")

    @abstractmethod
    def __serialize_seq__(self, seq: Sequence[_T]) -> None:
        ...

    _K = TypeVar("_K")
    _V = TypeVar("_V")

    @abstractmethod
    def __serialize_map__(self, map: Mapping[_K, _V]) -> None:
        ...

    @abstractmethod
    def __serialize_none__(self) -> None:
        ...
