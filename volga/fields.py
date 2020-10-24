from __future__ import annotations
from typing import Mapping

from volga.types import supportsDeser
from volga.types import T
from volga.format import Format


class Field(supportsDeser):
    """
    Provides methods for a data format to construct this
    field from any of the supported volga data types.
    """

    ...


class Bool(Field):

    value: bool

    def __init__(self, b: bool) -> None:
        self.value = b

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def __deserialize__(cls, format: Format) -> Bool:
        return format.__deserialize_bool__(cls)

    @classmethod
    def __from_bool__(cls, value: bool) -> T:
        return cls(value)

    @classmethod
    def __from_dict__(cls, d: Mapping[T, T]) -> T:
        raise NotImplementedError

    @classmethod
    def __from_int__(cls, value: int) -> T:
        raise NotImplementedError

    @classmethod
    def __from_float__(cls, value: float) -> T:
        raise NotImplementedError

    @classmethod
    def __from_str__(cls, value: str) -> T:
        raise NotImplementedError

    @classmethod
    def __from_none__(cls, value: None) -> T:
        raise NotImplementedError
