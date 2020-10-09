from __future__ import annotations
from abc import abstractmethod
from typing import Mapping, Protocol, Sequence, TYPE_CHECKING


if TYPE_CHECKING:
    from . import data


class canSerialize(Protocol):
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

    @abstractmethod
    def __serialize_seq__(self, seq: Sequence[data.VolgaT]) -> None:
        ...

    @abstractmethod
    def __serialize_map__(self, map: Mapping[data.VolgaT, data.VolgaT]) -> None:
        ...

    @abstractmethod
    def __serialize_none__(self) -> None:
        ...


class canDeserialize(Protocol):
    @abstractmethod
    def __deserialize_bool__(self, visitor: data.Visitor) -> data.VisitorResult:
        ...

    @abstractmethod
    def __deserialize_int__(self, visitor: data.Visitor) -> data.VisitorResult:
        ...

    @abstractmethod
    def __deserialize_float__(self, visitor: data.Visitor) -> data.VisitorResult:
        ...

    @abstractmethod
    def __deserialize_seq__(self, visitor: data.Visitor) -> data.VisitorResult:
        ...

    @abstractmethod
    def __deserialize_map__(self, visitor: data.Visitor) -> data.VisitorResult:
        ...

    @abstractmethod
    def __deserialize_str__(self, visitor: data.VisitorResult) -> data.VisitorResult:
        ...

    @abstractmethod
    def __deserialize_none__(self, visitor: data.Visitor) -> data.VisitorResult:
        ...


class Format(canSerialize, canDeserialize, Protocol):
    """
    A data format that can serialize and deserialize any data structure
    supported by volga.
    """

    # method to bypass primitives before calling serialize on value
    def serialize(self, value: data.VolgaT) -> None:
        if isinstance(value, bool):
            self.__serialize_bool__(value)
        elif isinstance(value, float):
            self.__serialize_float__(value)
        elif isinstance(value, int):
            self.__serialize_int__(value)
        elif isinstance(value, str):
            self.__serialize_str__(value)
        elif isinstance(value, Sequence):
            self.__serialize_seq__(value)
        elif isinstance(value, Mapping):
            self.__serialize_map__(value)
        elif value is None:
            self.__serialize_none__()
        else:
            value.serialize(self)
