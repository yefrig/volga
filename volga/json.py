from __future__ import annotations
from typing import Any, Mapping, Type, Union

import re

from typing_extensions import get_type_hints


from volga.format import Format
from volga.schema import Schema
from volga.fields import Str

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

    def parse_number(self) -> Union[int, float]:

        match = NUMBER_RE.match(self.s, self.idx)

        if match:
            integer, frac, exp = match.groups()
            if frac or exp:
                n = float(integer + (frac or "") + (exp or ""))
            else:
                n = int(integer)
            self.idx = match.end()
            return n
        else:
            raise RuntimeError("Expected int or float")

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

    def parse_null(self) -> None:
        idx = self.idx
        curr_char = self.s[idx]

        if curr_char == "n" and self.s[idx : idx + 4] == "null":
            self.idx += 5
            return None
        else:
            raise RuntimeError("Expected null")

    def __deserialize_str__(self, constructor: Type[Str]) -> str:

        return constructor.__from_str__(self.parse_str())

    def __deserialize_dict__(self, constructor: Type[User]) -> User:

        res: Mapping[str, str] = {}

        if self.s[self.idx] != "{":
            raise RuntimeError("Expected dict")

        # for each attribute in the schema

        attrs = get_type_hints(constructor, include_extras=True)
        for key in attrs:

            # skip past first {
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
            value = attrs[key].__deserialize__(self)

            res[parsed_key] = value

        return constructor.__from_dict__(res)


# TODO: move this back to schema using Field for testing
def deserialize(input: str, cls: Type[User]) -> Any:

    format = JSON(input)

    return cls.__deserialize__(format)


class User(Schema):

    name: Str

    def __repr__(self) -> str:
        return "User(name=" + self.name.__repr__() + ")"

    @classmethod
    def from_dict(cls: Type[User], d: Mapping[str, str]):
        instance = cls()
        for key in d:
            setattr(instance, key, d[key])
        return instance

    @classmethod
    def __deserialize__(cls: Type[User], format: JSON) -> User:
        return format.__deserialize_dict__(cls)

    @classmethod
    def __from_dict__(cls: Type[User], d: Mapping[str, str]) -> User:
        return cls.from_dict(d)


user = deserialize('{"name":"yefri"}', User)
print(user)
