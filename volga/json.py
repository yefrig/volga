from __future__ import annotations
from collections import deque
from typing import Any, Deque, TYPE_CHECKING, Type

import re

if TYPE_CHECKING:
    from volga.fields import Field

from volga.format import Format
from volga.fields import Str

# to be used for parsing JSON numbers
NUMBER_RE = re.compile(
    r"(-?(?:0|[1-9]\d*))(\.\d+)?([eE][-+]?\d+)?",
    (re.VERBOSE | re.MULTILINE | re.DOTALL),
)


class JSON(Format):
    """The class that implements the methods to serialize and deserialize JSONs.

    :param Format: A protocol that defines the methods data formats should support
        if they want to interact with volga's Field types.
    :type Format: [type]
    """

    def __init__(self, input: str) -> None:
        """[summary]

        :param input: [description]
        :type input: str
        """
        self.input: Deque[str] = deque(input)

    def __deserialize_bool__(self, expected: Field) -> bool:
        """[summary]

        :param expected: [description]
        :type expected: Field
        :return: [description]
        :rtype: bool
        """
        ...

    def __deserialize_int__(self, expected: Field) -> int:
        """[summary]

        :param expected: [description]
        :type expected: Field
        :return: [description]
        :rtype: int
        """
        ...

    def __deserialize_float__(self, expected: Field) -> float:
        """[summary]

        :param expected: [description]
        :type expected: Field
        :return: [description]
        :rtype: float
        """
        ...

    def __deserialize_str__(self, expected: Field) -> str:
        """[summary]

        :param expected: [description]
        :type expected: Field
        :return: [description]
        :rtype: str
        """
        ...

    def __deserialize_none__(self, expected: Field) -> Type[None]:
        """[summary]

        :param expected: [description]
        :type expected: Field
        :return: [description]
        :rtype: Type[None]
        """
        ...


# TODO: move this back to schema using Field for testing
def deserialize(input: str, field: Field) -> Any:

    format = JSON(input)

    return field.deserialize(format)


print(deserialize('"hello, this is a string!!!"', Str()))
