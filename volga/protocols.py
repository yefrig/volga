from __future__ import annotations

from typing import Protocol, TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from volga.format import Format


RT = TypeVar("RT")


class supportsDeserialization(Protocol):
    """This protocol defines methods to be implemented by data fields
    or data formats to be able to be deserialized to and from.
    """

    def __deserialize__(self, format: Format) -> RT:
        raise NotImplementedError

    def __deserialize_bool__(self, value: bool) -> RT:
        raise NotImplementedError

    def __deserialize_int__(self, value: int) -> RT:
        raise NotImplementedError

    def __deserialize_float__(self, value: float) -> RT:
        raise NotImplementedError

    def __deserialize_str__(self, value: str) -> RT:
        raise NotImplementedError

    def __deserialize_none__(self, value: None) -> RT:
        raise NotImplementedError
