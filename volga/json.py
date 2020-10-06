from typing import Mapping, Sequence, TypeVar

from serialize import Serialize
from serializer import Serializer

_T = TypeVar("_T", Serialize, bool, float, int, str, list, dict, None)

"""
    Map each of the volga's data model types to JSON
"""


class JSONSerializer(Serializer):

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

    def __serialize_seq__(self, seq: Sequence[_T]) -> None:
        self.output += "["

        for elem in seq:
            # add comma after first element
            if self.output[-1] != "[":
                self.output += ","

            _serialize_with_primitives(self, elem)

        self.output += "]"
        return

    def __serialize_map__(self, map: Mapping[_T, _T]) -> None:
        self.output += "{"

        for key in map.keys():
            # serialize key
            if self.output[-1] != "{":
                self.output += ","
            _serialize_with_primitives(self, key)

            # serialize value
            self.output += ":"
            _serialize_with_primitives(self, map[key])

        self.output += "}"
        return

    def __serialize_none__(self) -> None:
        self.output += "null"
        return


def to_string(value: _T) -> str:

    se = JSONSerializer()
    _serialize_with_primitives(se, value)

    return se.output


def _serialize_with_primitives(se: Serializer, value: _T) -> None:

    if isinstance(value, bool):
        se.__serialize_bool__(value)
    elif isinstance(value, float):
        se.__serialize_float__(value)
    elif isinstance(value, int):
        se.__serialize_int__(value)
    elif isinstance(value, list):
        se.__serialize_seq__(value)
    elif isinstance(value, dict):
        se.__serialize_map__(value)
    elif isinstance(value, str):
        se.__serialize_str__(value)
    elif value is None:
        se.__serialize_none__()
    else:
        value.serialize(se)
