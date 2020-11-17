from __future__ import annotations
from typing import Type, TypeVar

from volga.types import supportsDeser, T
from volga.format import Format

_T = TypeVar("_T")


class Schema(supportsDeser):
    def __str__(self) -> str:
        return str(vars(self))

    @classmethod
    def __deserialize__(cls: Type[_T], format: Format) -> _T:
        """deserialize schemas from dictionaries"""
        return format.__deserialize_dict__(cls)

    @classmethod
    def __from_dict__(cls, d: dict[T, T]) -> Schema:

        instance = cls()

        for key in d:
            setattr(instance, key.__str__(), d[key])
        return instance
