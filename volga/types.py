from __future__ import annotations

from abc import abstractmethod
from typing import Protocol, TYPE_CHECKING, Type, Any


if TYPE_CHECKING:
    from volga.format import Format


class supportsDeser(Protocol):
    """This protocol defines the entry point for objects to be deserializable"""

    @abstractmethod
    def __init__(self, value: Any) -> None:
        ...

    @abstractmethod
    def __deserialize__(self, format: Format) -> supportsDeser:
        raise NotImplementedError

    @classmethod
    def __from_bool__(cls: Type[supportsDeser], value: bool) -> supportsDeser:
        return cls(value)

    @classmethod
    def __from_int__(cls: Type[supportsDeser], value: int) -> supportsDeser:
        return cls(value)

    @classmethod
    def __from_float__(cls: Type[supportsDeser], value: float) -> supportsDeser:
        return cls(value)

    @classmethod
    def __from_str__(cls: Type[supportsDeser], value: str) -> supportsDeser:
        return cls(value)

    @classmethod
    def __from_none__(cls: Type[supportsDeser], value: Any) -> supportsDeser:
        return cls(value)

    @classmethod
    def __from_dict__(cls: Type[supportsDeser], d: dict[Any, Any]) -> supportsDeser:
        return cls(d)
