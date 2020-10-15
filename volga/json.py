from typing import Mapping, Sequence

from volga.data import Visitor, VisitorResult, VolgaT
from volga.format import Format


class JSON(Format):

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

    def __serialize_seq__(self, seq: Sequence[VolgaT]) -> None:
        self.output += "["

        for elem in seq:
            # add comma after first element
            if self.output[-1] != "[":
                self.output += ","

            self.serialize(elem)

        self.output += "]"
        return

    def __serialize_map__(self, map: Mapping[VolgaT, VolgaT]) -> None:
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

    def __deserialize_bool__(self, visitor: Visitor) -> VisitorResult:
        ...

    def __deserialize_int__(self, visitor: Visitor) -> VisitorResult:
        ...

    def __deserialize_float__(self, visitor: Visitor) -> VisitorResult:
        ...

    def __deserialize_seq__(self, visitor: Visitor) -> VisitorResult:
        ...

    def __deserialize_map__(self, visitor: Visitor) -> VisitorResult:
        ...

    def __deserialize_str__(self, visitor: VisitorResult) -> VisitorResult:
        ...

    def __deserialize_none__(self, visitor: Visitor) -> VisitorResult:
        ...


def to_string(value: VolgaT) -> str:

    format = JSON()
    format.serialize(value)

    return format.output


print(to_string({1: "a", 2: "b"}))
