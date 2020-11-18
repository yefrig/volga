from __future__ import annotations
from abc import ABC
from typing import Any

from volga.types import supportsDeser
from volga.format import Format


class Field(ABC):
    """
    Provides methods for a data format to construct this
    field from any of the supported volga data types.
    """


class Bool(int, Field, supportsDeser):
    def __init__(self, value: Any) -> None:
        super().__init__(value)

    def __repr__(self) -> str:
        return bool.__repr__(bool(self))

    def __deserialize__(self, format: Format) -> supportsDeser:
        return format.__deserialize_bool__(self.__class__)


class Int(int, Field, supportsDeser):
    def __init__(self, value: Any) -> None:
        super().__init__(value)

    def __deserialize__(self, format: Format) -> supportsDeser:
        return format.__deserialize_int__(self.__class__)


class Float(float, Field, supportsDeser):
    def __init__(self, value: Any) -> None:
        super().__init__(value)

    def __deserialize__(self, format: Format) -> supportsDeser:
        return format.__deserialize_float__(self.__class__)


class Str(str, Field, supportsDeser):
    def __init__(self, value: Any) -> None:
        super().__init__(value)

    def __deserialize__(self, format: Format) -> supportsDeser:
        return format.__deserialize_str__(self.__class__)


class Null(Field, supportsDeser):

    """ Null objects always and reliably "do nothing." """

    def __init__(self, value: Any) -> None:
        return None

    def __call__(self, *args: Any, **kwargs: Any) -> None:
        return None

    def __repr__(self) -> str:
        return "None"

    def __nonzero__(self) -> int:
        return 0

    def __deserialize__(self, format: Format) -> supportsDeser:
        return format.__deserialize_none__(self.__class__)

    def __eq__(self, other: Any):
        return other is None


class Dict(dict[Any, Any], Field, supportsDeser):
    def __init__(self, value: Any) -> None:
        super().__init__(value)

    def __deserialize__(self, format: Format) -> supportsDeser:
        return format.__deserialize_dict__(self.__class__)
