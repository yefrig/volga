from __future__ import annotations
from abc import abstractmethod
from typing import Protocol, TYPE_CHECKING, Type, TypeVar


if TYPE_CHECKING:
    from volga.format import Format


# represents a generic volga data type that can be deserialized
T = TypeVar("T", bound="supportsDeser")


class Constructor(Protocol):
    @classmethod
    def __from_bool__(cls: Type[T], value: bool) -> T:
        raise NotImplementedError

    @classmethod
    def __from_int__(cls: Type[T], value: int) -> T:
        raise NotImplementedError

    @classmethod
    def __from_float__(cls: Type[T], value: float) -> T:
        raise NotImplementedError

    @classmethod
    def __from_str__(cls: Type[T], value: str) -> T:
        raise NotImplementedError

    @classmethod
    def __from_none__(cls: Type[T]) -> T:
        raise NotImplementedError

    @classmethod
    def __from_dict__(cls: Type[T], d: dict[T, T]) -> T:
        raise NotImplementedError


class supportsDeser(Constructor, Protocol):
    """This protocol defines the entry point for objects to be deserializable"""

    @classmethod
    @abstractmethod
    def __deserialize__(cls: Type[T], format: Format) -> T:
        raise NotImplementedError
