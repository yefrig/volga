from __future__ import annotations

from abc import abstractmethod
from typing import Protocol, TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from volga.fields import Field

"""
    Each data format can decide what kind of Python data type they return
    for each supported Volga type. This generic return type is represented
    by RT.
"""
RT = TypeVar("RT")


class Format(Protocol):
    """This protocol defines the methods data formats should support
        if they want to interact with volga's Field types.

    :raises NotImplementedError: Classes that subclass this protocol
        should not called any of these functions using super().
    """

    @abstractmethod
    def __deserialize_bool__(self, field: Field) -> RT:
        raise NotImplementedError

    @abstractmethod
    def __deserialize_int__(self, field: Field) -> RT:
        raise NotImplementedError

    @abstractmethod
    def __deserialize_float__(self, field: Field) -> RT:
        raise NotImplementedError

    @abstractmethod
    def __deserialize_str__(self, field: Field) -> RT:
        raise NotImplementedError

    @abstractmethod
    def __deserialize_none__(self, field: Field) -> RT:
        raise NotImplementedError
