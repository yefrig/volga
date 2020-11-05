from __future__ import annotations

from typing import Protocol, TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from volga.format import Format


RT = TypeVar("RT")


class supportsDeserialization(Protocol):
    """This protocol defines methods to be implemented by data fields
    or data formats so they can be deserialized to and from.

    :param Protocol: [description]
    :type Protocol: [type]
    """

    def deserialize(self, format: Format) -> RT:
        """[summary]

        :param format: [description]
        :type format: Format
        :raises NotImplementedError: [description]
        :return: [description]
        :rtype: RT
        """
        raise NotImplementedError

    def __deserialize_bool__(self, value: bool) -> RT:
        """[summary]

        :param value: [description]
        :type value: bool
        :raises NotImplementedError: [description]
        :return: [description]
        :rtype: RT
        """
        raise NotImplementedError

    def __deserialize_int__(self, value: int) -> RT:
        """[summary]

        :param value: [description]
        :type value: int
        :raises NotImplementedError: [description]
        :return: [description]
        :rtype: RT
        """
        raise NotImplementedError

    def __deserialize_float__(self, value: float) -> RT:
        """[summary]

        :param value: [description]
        :type value: float
        :raises NotImplementedError: [description]
        :return: [description]
        :rtype: RT
        """
        raise NotImplementedError

    def __deserialize_str__(self, value: str) -> RT:
        """[summary]

        :param value: [description]
        :type value: str
        :raises NotImplementedError: [description]
        :return: [description]
        :rtype: RT
        """
        raise NotImplementedError

    def __deserialize_none__(self, value: None) -> RT:
        """[summary]

        :param value: [description]
        :type value: None
        :raises NotImplementedError: [description]
        :return: [description]
        :rtype: RT
        """
        raise NotImplementedError
