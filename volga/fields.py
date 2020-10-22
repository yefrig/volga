from __future__ import annotations


from typing import TYPE_CHECKING, Type
from volga.protocols import supportsDeserialization

if TYPE_CHECKING:
    from volga.format import Format


class Field(supportsDeserialization):
    ...


class Bool(Field):
    def deserialize(self, format: Format) -> bool:
        return format.__deserialize_bool__(self)

    def __deserialize_bool__(self, b: bool) -> bool:
        ...


class Int(Field):
    def deserialize(self, format: Format) -> int:
        return format.__deserialize_int__(self)

    def __deserialize_int__(self, n: int) -> int:
        ...


class Float(Field):
    def deserialize(self, format: Format) -> float:
        return format.__deserialize_float__(self)

    def __deserialize_float__(self, n: float) -> float:
        ...


class Str(Field):
    def deserialize(self, format: Format) -> str:
        return format.__deserialize_str__(self)

    def __deserialize_str__(self, s: str) -> str:
        ...


class Null(Field):
    def deserialize(self, format: Format) -> Type[None]:
        return format.__deserialize_none__(self)

    def __deserialize_none__(self, a: Type[None]) -> Type[None]:
        ...
