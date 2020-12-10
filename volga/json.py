from __future__ import annotations
from typing import TYPE_CHECKING, Type

import re

if TYPE_CHECKING:
    import volga.types as types

from typing import get_type_hints
import volga.fields as fields


import volga.format as format
import volga.exceptions as exceptions

RE_FLAGS = re.VERBOSE | re.MULTILINE | re.DOTALL

# parse string after first '"' and terminate by '"'
STRING_RE = re.compile(r'(.*?)(")', RE_FLAGS)

# to be used for parsing JSON numbers
NUMBER_RE = re.compile(
    r"(-?(?:0|[1-9]\d*))(\.\d+)?([eE][-+]?\d+)?",
    RE_FLAGS,
)


class JSON(format.Format):
    """hello this a json file

    Args:
        Format ([type]): [description]
    """

    def __init__(self, input: str) -> None:
        self.s: str = input
        self.idx: int = 0

    def _parse_bool(self) -> bool:

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
            raise exceptions.ParsingError("Expected bool")

    def _parse_float(self) -> float:

        match = NUMBER_RE.match(self.s, self.idx)

        if match:
            integer, frac, exp = match.groups()

            n = float(integer + (frac or "") + (exp or ""))
            self.idx = match.end()
            return n
        else:
            raise exceptions.ParsingError("Expected float")

    def _parse_int(self) -> int:

        match = NUMBER_RE.match(self.s, self.idx)

        if match:
            integer, frac, exp = match.groups()
            if frac or exp:
                raise exceptions.ParsingError("Expected integer value.")
            else:
                n = int(integer)
            self.idx = match.end()
            return n
        else:
            raise exceptions.ParsingError("Expected int")

    def _parse_str(self) -> str:

        if type(self.s) != str:
            raise exceptions.ParsingError("Expected String, not " + str(type(self.s)))

        if self.s[self.idx] != '"':
            raise exceptions.ParsingError("Expected String")

        # skip past first "
        chunk = STRING_RE.match(self.s, self.idx + 1)

        if chunk is None:
            raise exceptions.ParsingError("Unterminated string.")

        content, _ = chunk.groups()
        self.idx = chunk.end()
        return content

    def _parse_none(self) -> None:
        idx = self.idx
        curr_char = self.s[idx]

        if curr_char == "n" and self.s[idx : idx + 4] == "null":
            self.idx += 5
            return None
        else:
            raise exceptions.ParsingError("Expected null")

    def __deserialize_str__(
        self, constructor: Type[types.supportsDeser]
    ) -> types.supportsDeser:
        return constructor.__from_str__(self._parse_str())

    def __deserialize_dict__(
        self, constructor: Type[types.supportsDeser]
    ) -> types.supportsDeser:

        res = {}

        if self.s[self.idx] != "{":
            raise exceptions.ParsingError("Expected dict")

        # for each attribute in the schema

        attrs = get_type_hints(constructor, include_extras=True)
        for key in attrs:

            # skip past first { and subsequent ,
            chunk = STRING_RE.match(self.s, self.idx + 2)

            if chunk is None:
                raise exceptions.ParsingError("Expected key string.")

            parsed_key, _ = chunk.groups()
            self.idx = chunk.end()

            assert parsed_key == key

            if self.s[self.idx] != ":":
                raise exceptions.ParsingError("Expected value for key")
            self.idx += 1

            # parse the value according to schema
            print(attrs[key])
            value = self.dispatch(attrs[key])

            res[fields.Str(parsed_key)] = value

        return constructor.__from_dict__(res)

    def __deserialize_bool__(
        self, constructor: Type[types.supportsDeser]
    ) -> types.supportsDeser:
        return constructor.__from_bool__(self._parse_bool())

    def __deserialize_int__(
        self, constructor: Type[types.supportsDeser]
    ) -> types.supportsDeser:
        return constructor.__from_int__(self._parse_int())

    def __deserialize_float__(
        self, constructor: Type[types.supportsDeser]
    ) -> types.supportsDeser:
        return constructor.__from_float__(self._parse_float())

    def __deserialize_none__(
        self, constructor: Type[types.supportsDeser]
    ) -> types.supportsDeser:
        # consume null
        self._parse_none()
        return constructor.__from_none__(None)

    def dispatch(self, cls: Type[types.supportsDeser]) -> types.supportsDeser:
        if issubclass(cls, fields.Bool):
            return cls(False).__deserialize__(self)
        elif issubclass(cls, fields.Int):
            return cls(0).__deserialize__(self)
        elif issubclass(cls, fields.Float):
            return cls(0.0).__deserialize__(self)
        elif issubclass(cls, fields.Str):
            return cls("").__deserialize__(self)
        elif issubclass(cls, fields.Null):
            return cls(None).__deserialize__(self)
        else:
            return cls({}).__deserialize__(self)


def deserialize(input: str, cls: Type[types.supportsDeser]) -> types.supportsDeser:
    """Deserialize any valid input into an instance of `cls`.

    Args:
        input (str): A string composed of the input to be deserialized.
        cls (Type[types.supportsDeser]): The class from which to create an instance for the deserialized input.

    Returns:
        types.supportsDeser: An instance of `cls` deserialized from input `input`.
    """

    format = JSON(input)

    # initialize empty instance to dispatch deserialize
    # TODO: investigate why protocol is not working with class method

    return format.dispatch(cls)
