from __future__ import annotations

from abc import abstractmethod
from typing import Protocol, Type

from volga.types import T


class Format(Protocol):
    """This protocol defines the methods data formats should support
        if they want to interact with volga's types.
        if they want to interact with volga's Field types.

    :raises NotImplementedError: Classes that subclass this protocol
        should not called any of these functions using super().
    """

    @abstractmethod
    def __deserialize_bool__(self, cls: Type[T]) -> T:
        raise NotImplementedError

    @abstractmethod
    def __deserialize_int__(self, cls: Type[T]) -> T:
        raise NotImplementedError

    @abstractmethod
    def __deserialize_float__(self, cls: Type[T]) -> T:
        raise NotImplementedError

    @abstractmethod
    def __deserialize_str__(self, cls: Type[T]) -> T:
        raise NotImplementedError

    @abstractmethod
    def __deserialize_dict__(self, cls: Type[T]) -> T:
        raise NotImplementedError

    @abstractmethod
    def __deserialize_none__(self, cls: Type[T]) -> T:
        raise NotImplementedError
