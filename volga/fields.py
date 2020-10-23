from typing import Any, TYPE_CHECKING, Type

if TYPE_CHECKING:
    from volga.format import Format


class Field:
    """
    Provides methods for a data format to construct this
    field from any of the supported volga data types.
    """

    ...


class Bool(Field):
    def __deserialize__(self, format: Format) -> bool:
        # hint data format to
        return format.__deserialize_bool__(self)

    def __deserialize_bool__(self, b: bool) -> bool:
        return bool(b)


class Int(Field):
    def __deserialize__(self, format: Format) -> int:
        return format.__deserialize_int__(self)

    def __deserialize_int__(self, n: int) -> int:
        return int(n)


class Float(Field):
    def __deserialize__(self, format: Format) -> float:
        return format.__deserialize_float__(self)

    def __deserialize_float__(self, n: float) -> float:
        return float(n)


class Str(Field):
    @classmethod
    def __deserialize__(cls: Type[Any], format: Format) -> str:
        return format.__deserialize_str__(cls)

    @staticmethod
    def __from_str__(s: str) -> str:
        return str(s)


class Null(Field):
    def __deserialize__(self, format: Format) -> Type[None]:
        return format.__deserialize_none__(self)

    def __deserialize_none__(self, a: Type[None]) -> Type[None]:
        return a
