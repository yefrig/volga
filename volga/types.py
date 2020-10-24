from __future__ import annotations

from abc import abstractmethod

from typing import Mapping, Protocol, TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from volga.format import Format

# represents a generic volga data type that can be deserialized
T = TypeVar("T", bound="supportsDeser")


class Constructor(Protocol):
    @classmethod
    @abstractmethod
    def __from_dict__(cls, d: Mapping[T, T]) -> T:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def __from_bool__(cls, value: bool) -> T:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def __from_int__(cls, value: int) -> T:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def __from_float__(cls, value: float) -> T:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def __from_str__(cls, value: str) -> T:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def __from_none__(cls, value: None) -> T:
        raise NotImplementedError


class supportsDeser(Constructor, Protocol):
    """This protocol defines the entry point for objects to be deserializable"""

    @classmethod
    @abstractmethod
    def __deserialize__(cls, format: Format) -> T:
        raise NotImplementedError
