from __future__ import annotations

from abc import ABC
from typing import Any

import volga.types as types
import volga.format as format


class Field(ABC):
    """Base class that represents a volga type that can be deserialized from
    any data format supported by Volga.

    All Field types subclass the respective python primitives. This is needed
    because python primitives cannot be extended to be made deserializable by
    implementing __deserialize__.
    """


class Bool(int, Field, types.supportsDeser):
    """The Bool type for volga that supports deserialization.
    This type subclasses int instead of bool since the bool primitive
    cannot be subclassed in Python.
    """

    def __init__(self, value: Any) -> None:
        super().__init__(value)

    def __repr__(self) -> str:
        return bool.__repr__(bool(self))

    def __deserialize__(self, format: format.Format) -> types.supportsDeser:
        """Deserialize this value from the given format.

        Args:
            format (Format): The data format that wants to deserialize this class.

        Returns:
            Bool: A new instance of this class deserialized by the data format
        """
        return format.__deserialize_bool__(self.__class__)


class Int(int, Field, types.supportsDeser):
    """The Int type for volga that supports deserialization.

    This class is equivalent with the int primitive."""

    def __init__(self, value: Any) -> None:
        super().__init__(value)

    def __deserialize__(self, format: format.Format) -> types.supportsDeser:
        """Deserialize this value from the given format.

        Args:
            format (Format): The data format that wants to deserialize this class.

        Returns:
            Int: A new instance of this class deserialized by the data format
        """
        return format.__deserialize_int__(self.__class__)


class Float(float, Field, types.supportsDeser):
    """The Float type for volga that supports deserialization.

    This class is equivalent with the float primitive."""

    def __init__(self, value: Any) -> None:
        super().__init__(value)

    def __deserialize__(self, format: format.Format) -> types.supportsDeser:
        """Deserialize this value from the given format.

        Args:
            format (Format): The data format that wants to deserialize this class.

        Returns:
            Float: A new instance of this class deserialized by the data format
        """
        return format.__deserialize_float__(self.__class__)


class Str(str, Field, types.supportsDeser):
    """The Str type for volga that supports deserialization.

    This class is equivalent with the str primitive."""

    def __init__(self, value: Any) -> None:
        super().__init__(value)

    def __deserialize__(self, format: format.Format) -> types.supportsDeser:
        """Deserialize this value from the given format.

        Args:
            format (Format): The data format that wants to deserialize this class.

        Returns:
            Str: A new instance of this class deserialized by the data format
        """
        return format.__deserialize_str__(self.__class__)


class Null(Field, types.supportsDeser):
    """Null objects always and reliably 'do nothing'.

    This class is equivalent with None."""

    def __init__(self, value: Any) -> None:
        return None

    def __call__(self, *args: Any, **kwargs: Any) -> None:
        return None

    def __repr__(self) -> str:
        return "None"

    def __nonzero__(self) -> int:
        return 0

    def __deserialize__(self, format: format.Format) -> types.supportsDeser:
        """Deserialize this value from the given format.

        Args:
            format (Format): The data format that wants to deserialize this class.

        Returns:
            Null: A new instance of this class deserialized by the data format
        """
        return format.__deserialize_none__(self.__class__)

    def __eq__(self, other: Any):
        return other is None


class Dict(dict[Any, Any], Field, types.supportsDeser):
    """The Dict type for volga that supports deserialization.

    This class is equivalent with the dict primitive."""

    def __init__(self, value: Any) -> None:
        super().__init__(value)

    def __deserialize__(self, format: format.Format) -> types.supportsDeser:
        """Deserialize this value from the given format.

        Args:
            format (Format): The data format that wants to deserialize this class.

        Returns:
            Dict: A new instance of this class deserialized by the data format
        """
        return format.__deserialize_dict__(self.__class__)
