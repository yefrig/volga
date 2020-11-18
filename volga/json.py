from __future__ import annotations
from typing import TYPE_CHECKING, Type

import re

if TYPE_CHECKING:
    from volga.types import supportsDeser

from typing import get_type_hints
from volga.fields import Bool, Float, Int, Null, Str


from volga.format import Format

RE_FLAGS = re.VERBOSE | re.MULTILINE | re.DOTALL

# parse string after first '"' and terminate by '"'
STRING_RE = re.compile(r'(.*?)(")', RE_FLAGS)

# to be used for parsing JSON numbers
NUMBER_RE = re.compile(
    r"(-?(?:0|[1-9]\d*))(\.\d+)?([eE][-+]?\d+)?",
    RE_FLAGS,
)


class JSON(Format):
    def __init__(self, input: str) -> None:
        self.s: str = input
        self.idx: int = 0

    def parse_bool(self) -> bool:

        idx = self.idx
        curr_char = self.s[idx]

        if curr_char == "t" and self.s[idx : idx + 4] == "true":
            # move to 1 pass the last letter of true
            self.idx += 5
            return True
        elif curr_char == "f" and self.s[idx : idx + 5] == "false":
            self.idx += 6
            return False
        else:
            raise RuntimeError("Expected bool")

    def parse_float(self) -> float:

        match = NUMBER_RE.match(self.s, self.idx)

        if match:
            integer, frac, exp = match.groups()

            n = float(integer + (frac or "") + (exp or ""))
            self.idx = match.end()
            return n
        else:
            raise RuntimeError("Expected float")

    def parse_int(self) -> int:

        match = NUMBER_RE.match(self.s, self.idx)

        if match:
            integer, frac, exp = match.groups()
            if frac or exp:
                raise RuntimeError("Expected integer value.")
            else:
                n = int(integer)
            self.idx = match.end()
            return n
        else:
            raise RuntimeError("Expected int")

    def parse_str(self) -> str:

        if self.s[self.idx] != '"':
            raise RuntimeError("Expected String")

        # skip past first "
        chunk = STRING_RE.match(self.s, self.idx + 1)

        if chunk is None:
            raise RuntimeError("Unterminated string.")

        content, _ = chunk.groups()
        self.idx = chunk.end()
        return content

    def parse_none(self) -> None:
        idx = self.idx
        curr_char = self.s[idx]

        if curr_char == "n" and self.s[idx : idx + 4] == "null":
            self.idx += 5
            return None
        else:
            raise RuntimeError("Expected null")

    def __deserialize_str__(self, constructor: Type[supportsDeser]) -> supportsDeser:
        return constructor.__from_str__(self.parse_str())

    def __deserialize_dict__(self, constructor: Type[supportsDeser]) -> supportsDeser:

        res = {}

        if self.s[self.idx] != "{":
            raise RuntimeError("Expected dict")

        # for each attribute in the schema

        attrs = get_type_hints(constructor, include_extras=True)
        for key in attrs:

            # skip past first { and subsequent ,
            chunk = STRING_RE.match(self.s, self.idx + 2)

            if chunk is None:
                raise RuntimeError("Expected key string.")

            parsed_key, _ = chunk.groups()
            self.idx = chunk.end()

            assert parsed_key == key

            if self.s[self.idx] != ":":
                raise RuntimeError("Expected value for key")
            self.idx += 1

            # parse the value according to schema
            print(attrs[key])
            value = self.dispatch(attrs[key])

            res[Str(parsed_key)] = value

        return constructor.__from_dict__(res)

    def __deserialize_bool__(self, constructor: Type[supportsDeser]) -> supportsDeser:
        return constructor.__from_bool__(self.parse_bool())

    def __deserialize_int__(self, constructor: Type[supportsDeser]) -> supportsDeser:
        return constructor.__from_int__(self.parse_int())

    def __deserialize_float__(self, constructor: Type[supportsDeser]) -> supportsDeser:
        return constructor.__from_float__(self.parse_float())

    def __deserialize_none__(self, constructor: Type[supportsDeser]) -> supportsDeser:
        # consume null
        self.parse_none()
        return constructor.__from_none__(None)

    def dispatch(self, cls: Type[supportsDeser]) -> supportsDeser:
        if issubclass(cls, Bool):
            return cls(False).__deserialize__(self)
        elif issubclass(cls, Int):
            return cls(0).__deserialize__(self)
        elif issubclass(cls, Float):
            return cls(0.0).__deserialize__(self)
        elif issubclass(cls, Str):
            return cls("").__deserialize__(self)
        elif issubclass(cls, Null):
            return cls(None).__deserialize__(self)
        else:
            return cls({}).__deserialize__(self)


def deserialize(input: str, cls: Type[supportsDeser]) -> supportsDeser:

    format = JSON(input)

    # initialize empty instance to dispatch deserialize
    # TODO: investigate why protocol is not working with class method

    return format.dispatch(cls)
