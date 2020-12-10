from __future__ import annotations

from abc import abstractmethod
from typing import Protocol, TYPE_CHECKING, Type

if TYPE_CHECKING:
    import volga.types as types


class Format(Protocol):
    """A protocol that defines a data format that can deserialize any data
    structure supported by volga.
    """

    @abstractmethod
    def __deserialize_bool__(
        self, cls: Type[types.supportsDeser]
    ) -> types.supportsDeser:
        """Hint that cls type is expecting a `bool` value.

        Args:
            cls (Type[types.]): the class that will instantiated by this format.

        Raises:
            NotImplementedError: Raised when used by formats that have not implemented this method.

        Returns:
            types.: Returns a deseriazable instance of `cls`.
        """
        raise NotImplementedError

    @abstractmethod
    def __deserialize_int__(
        self, cls: Type[types.supportsDeser]
    ) -> types.supportsDeser:
        """Hint that cls type is expecting a `int` value.

        Args:
            cls (Type[types.]): the class that will instantiated by this format.

        Raises:
            NotImplementedError: Raised when used by formats that have not implemented this method.

        Returns:
            types.: Returns a deseriazable instance of `cls`.
        """
        raise NotImplementedError

    @abstractmethod
    def __deserialize_float__(
        self, cls: Type[types.supportsDeser]
    ) -> types.supportsDeser:
        """Hint that cls type is expecting a `float` value.

        Args:
            cls (Type[types.]): the class that will instantiated by this format.

        Raises:
            NotImplementedError: Raised when used by formats that have not implemented this method.

        Returns:
            types.: Returns a deseriazable instance of `cls`.
        """
        raise NotImplementedError

    @abstractmethod
    def __deserialize_str__(
        self, cls: Type[types.supportsDeser]
    ) -> types.supportsDeser:
        """Hint that cls type is expecting a `str` value.

        Args:
            cls (Type[types.]): the class that will instantiated by this format.

        Raises:
            NotImplementedError: Raised when used by formats that have not implemented this method.

        Returns:
            types.: Returns a deseriazable instance of `cls`.
        """
        raise NotImplementedError

    @abstractmethod
    def __deserialize_dict__(
        self, cls: Type[types.supportsDeser]
    ) -> types.supportsDeser:
        """Hint that cls type is expecting a `dict` value.

        Args:
            cls (Type[types.]): the class that will instantiated by this format.

        Raises:
            NotImplementedError: Raised when used by formats that have not implemented this method.

        Returns:
            types.: Returns a deseriazable instance of `cls`.
        """
        raise NotImplementedError

    @abstractmethod
    def __deserialize_none__(
        self, cls: Type[types.supportsDeser]
    ) -> types.supportsDeser:
        """Hint that cls type is expecting a `None` value.

        Args:
            cls (Type[types.]): the class that will instantiated by this format.

        Raises:
            NotImplementedError: Raised when used by formats that have not implemented this method.

        Returns:
            types.: Returns a deseriazable instance of `cls`.
        """
        raise NotImplementedError
