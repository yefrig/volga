from __future__ import annotations


from typing import TYPE_CHECKING, Type
from volga.protocols import supportsDeserialization

if TYPE_CHECKING:
    from volga.format import Format


class Field(supportsDeserialization):
    """The base class all fields should extend from.

    :param supportsDeserialization: [description]
    :type supportsDeserialization: [type]
    """

    ...


class Bool(Field):
    """Wrapper class to serialize and deserialize boolean types.

    :param Field: The base class all fields should extend from.
    :type Field: [type]
    """

    def deserialize(self, format: Format) -> bool:
        return format.__deserialize_bool__(self)

    def __deserialize_bool__(self, b: bool) -> bool:
        ...


class Int(Field):
    """Wrapper class to serialize and deserialize integer types.

    :param Field: The base class all fields should extend from.
    :type Field: [type]
    """

    def deserialize(self, format: Format) -> int:
        return format.__deserialize_int__(self)

    def __deserialize_int__(self, n: int) -> int:
        ...


class Float(Field):
    """Wrapper class to serialize and deserialize float types.

    :param Field: The base class all fields should extend from.
    :type Field: [type]
    """

    def deserialize(self, format: Format) -> float:
        return format.__deserialize_float__(self)

    def __deserialize_float__(self, n: float) -> float:
        ...


class Str(Field):
    """Wrapper class to serialize and deserialize string types.

    :param Field: The base class all fields should extend from.
    :type Field: [type]
    """

    def deserialize(self, format: Format) -> str:
        return format.__deserialize_str__(self)

    def __deserialize_str__(self, s: str) -> str:
        ...


class Null(Field):
    """Wrapper class to serialize and deserialize Null values.

    :param Field: The base class all fields should extend from.
    :type Field: [type]
    """

    def deserialize(self, format: Format) -> Type[None]:
        return format.__deserialize_none__(self)

    def __deserialize_none__(self, a: Type[None]) -> Type[None]:
        ...
