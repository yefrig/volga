from __future__ import annotations
from typing import Mapping, Sequence, TYPE_CHECKING

from . import format


if TYPE_CHECKING:
    from . import data


class JSON(format.Format):

    output: str = ""

    def __serialize_bool__(self, value: bool) -> None:
        self.output += "true" if value else "false"
        return

    def __serialize_float__(self, value: float) -> None:
        self.output += str(value)
        return

    def __serialize_int__(self, value: int) -> None:
        self.output += str(value)
        return

    def __serialize_str__(self, s: str) -> None:
        self.output += '"'
        self.output += s
        self.output += '"'
        return

    def __serialize_seq__(self, seq: Sequence[data.VolgaT]) -> None:
        self.output += "["

        for elem in seq:
            # add comma after first element
            if self.output[-1] != "[":
                self.output += ","

            self.serialize(elem)

        self.output += "]"
        return

    def __serialize_map__(self, map: Mapping[data.VolgaT, data.VolgaT]) -> None:
        self.output += "{"

        for key in map.keys():
            # serialize key
            if self.output[-1] != "{":
                self.output += ","
            self.serialize(key)

            # serialize value
            self.output += ":"
            self.serialize(map[key])

        self.output += "}"
        return

    def __serialize_none__(self) -> None:
        self.output += "null"
        return

    def __deserialize_bool__(self, visitor: data.Visitor) -> data.VisitorResult:
        ...

    def __deserialize_int__(self, visitor: data.Visitor) -> data.VisitorResult:
        ...

    def __deserialize_float__(self, visitor: data.Visitor) -> data.VisitorResult:
        ...

    def __deserialize_seq__(self, visitor: data.Visitor) -> data.VisitorResult:
        ...

    def __deserialize_map__(self, visitor: data.Visitor) -> data.VisitorResult:
        ...

    def __deserialize_str__(self, visitor: data.VisitorResult) -> data.VisitorResult:
        ...

    def __deserialize_none__(self, visitor: data.Visitor) -> data.VisitorResult:
        ...


def to_string(value: data.VolgaT) -> str:

    format = JSON()
    format.serialize(value)

    return format.output
