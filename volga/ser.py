from abc import abstractmethod
from typing import Protocol, TypeVar

_T = TypeVar("_T")


class SerializeSeq(Protocol[_T]):
    @abstractmethod
    def __serialize_element__(self, value: _T) -> None:
        ...

    @abstractmethod
    def __end__(self) -> None:
        ...


_K = TypeVar("_K")
_V = TypeVar("_V")


# TODO: rename to map and update data model
class SerializeDict(Protocol[_T]):
    @abstractmethod
    def __serialize_entry__(self, k: _K, v: _V) -> None:
        ...

    @abstractmethod
    def __end__(self) -> None:
        ...


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
    def __serialize_list__(self) -> SerializeSeq:
        ...

    @abstractmethod
    def __serialize_dict__(self) -> SerializeDict:
        ...

    @abstractmethod
    def __serialize_none__(self) -> None:
        ...
