from abc import abstractmethod
from typing import Sequence, Mapping, Protocol, TypeVar, Union
from volga.format import Format

VisitorResult = TypeVar("VisitorResult")

# Recursive Data type or primitives
VolgaT = Union[
    "Data", bool, int, float, str, None, Sequence["VolgaT"], Mapping["VolgaT", "VolgaT"]
]


"""
    A data structure that can be serialized and deserialized into any data
    format supported by volga.
"""


class supportsDeserialization(Protocol):
    pass


class supportsSerialization(Protocol):
    @abstractmethod
    def serialize(self, format: Format) -> None:
        ...


class Data(supportsSerialization, supportsDeserialization, Protocol):
    pass


class Visitor(Protocol):
    @abstractmethod
    def __visit_bool__(self, visitor: bool) -> VisitorResult:
        ...

    @abstractmethod
    def __visit_int__(self, value: int) -> VisitorResult:
        ...

    @abstractmethod
    def __visit_float__(self, value: float) -> VisitorResult:
        ...

    @abstractmethod
    def __visit_str__(self, s: str) -> VisitorResult:
        ...

    @abstractmethod
    def __visit_seq__(self, seq: Sequence[VolgaT]) -> VisitorResult:
        ...

    @abstractmethod
    def __visit_map__(self, map: Mapping[VolgaT, VolgaT]) -> VisitorResult:
        ...

    @abstractmethod
    def __visit_none__(self) -> VisitorResult:
        ...
