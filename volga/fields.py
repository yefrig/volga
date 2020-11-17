from __future__ import annotations
from typing import Any, Type, TypeVar

from volga.types import T, supportsDeser
from volga.format import Format


class Field(supportsDeser):
    """
    Provides methods for a data format to construct this
    field from any of the supported volga data types.
    """

    ...


# needed to match return type for class method from cls
_T = TypeVar("_T")


class Bool(int, Field):
    def __repr__(self) -> str:
        return bool.__repr__(bool(self))

    @classmethod
    def __deserialize__(cls: Type[_T], format: Format) -> _T:
        return format.__deserialize_bool__(cls)

    @classmethod
    def __from_bool__(cls, value: bool) -> Bool:
        return cls(value)

    @classmethod
    def __from_int__(cls, value: int) -> Bool:
        return cls(value)

    @classmethod
    def __from_float__(cls, value: float) -> Bool:
        return cls(value)


class Int(int, Field):
    @classmethod
    def __deserialize__(cls: Type[_T], format: Format) -> _T:
        return format.__deserialize_int__(cls)

    @classmethod
    def __from_bool__(cls, value: bool) -> Int:
        return cls(value)

    @classmethod
    def __from_int__(cls, value: int) -> Int:
        return cls(value)

    @classmethod
    def __from_float__(cls, value: float) -> Int:
        return cls(value)

    @classmethod
    def __from_str__(cls, value: str) -> Int:
        return cls(value)


class Float(float, Field):
    @classmethod
    def __deserialize__(cls: Type[_T], format: Format) -> _T:
        return format.__deserialize_float__(cls)

    @classmethod
    def __from_bool__(cls, value: bool) -> Float:
        return cls(value)

    @classmethod
    def __from_int__(cls, value: int) -> Float:
        return cls(value)

    @classmethod
    def __from_float__(cls, value: float) -> Float:
        return cls(value)

    @classmethod
    def __from_str__(cls, value: str) -> Float:
        return cls(value)


class Str(str, Field):
    @classmethod
    def __deserialize__(cls: Type[_T], format: Format) -> _T:
        return format.__deserialize_str__(cls)

    @classmethod
    def __from_bool__(cls, value: bool) -> Str:
        return cls(value)

    @classmethod
    def __from_int__(cls, value: int) -> Str:
        return cls(value)

    @classmethod
    def __from_float__(cls, value: float) -> Str:
        return cls(value)

    @classmethod
    def __from_str__(cls, value: str) -> Str:
        return cls(value)

    @classmethod
    def __from_none__(cls) -> Str:
        return cls(None)

    @classmethod
    def __from_dict__(cls, d: dict[T, T]) -> Str:
        return cls(d)


class Null(Field):

    """ Null objects always and reliably "do nothing." """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        return None

    def __call__(self, *args: Any, **kwargs: Any) -> None:
        return None

    def __repr__(self) -> str:
        return "None"

    def __nonzero__(self) -> int:
        return 0

    @classmethod
    def __deserialize__(cls: Type[_T], format: Format) -> _T:
        return format.__deserialize_none__(cls)

    @classmethod
    def __from_none__(cls) -> Null:
        return cls(None)


class Dict(dict[T, T], Field):
    @classmethod
    def __deserialize__(cls: Type[_T], format: Format) -> _T:
        return format.__deserialize_dict__(cls)

    @classmethod
    def __from_dict__(cls, d: dict[T, T]) -> Dict[T]:
        return cls(d)
