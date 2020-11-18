from __future__ import annotations
from typing import Any

from volga.types import supportsDeser
from volga.format import Format


class Schema(supportsDeser):
    def __init__(self, d: dict[Any, Any]) -> None:
        for key in d:
            setattr(self, key.__str__(), d[key])

    def __str__(self) -> str:
        return str(vars(self))

    @classmethod
    def __deserialize__(cls, format: Format) -> supportsDeser:
        """deserialize schemas from dictionaries"""
        return format.__deserialize_dict__(cls)
