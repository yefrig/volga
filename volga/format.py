from typing import Mapping, Protocol, Sequence
from abc import abstractmethod
from volga.data import Visitor
from volga.data import VisitorResult, VolgaT


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
    def __serialize_seq__(self, seq: Sequence[VolgaT]) -> None:
        ...

    @abstractmethod
    def __serialize_map__(self, map: Mapping[VolgaT, VolgaT]) -> None:
        ...

    @abstractmethod
    def __serialize_none__(self) -> None:
        ...


class canDeserialize(Protocol):
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
    def __deserialize_str__(self, visitor: VisitorResult) -> VisitorResult:
        ...

    @abstractmethod
    def __deserialize_none__(self, visitor: Visitor) -> VisitorResult:
        ...


class Format(canSerialize, canDeserialize, Protocol):
    """
    A data format that can serialize and deserialize any data structure
    supported by volga.
    """

    # method to bypass primitives before calling serialize on value
    def serialize(self, value: VolgaT) -> None:
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
