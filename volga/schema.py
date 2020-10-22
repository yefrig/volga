from volga.format import Format
from volga.protocols import supportsDeserialization


class Schema(supportsDeserialization):
    """[summary]

    :param supportsDeserialization: [description]
    :type supportsDeserialization: [type]
    """

    def __init__(self) -> None:
        """[summary]"""
        ...

    def __deserialize__(self, format: Format) -> None:
        """[summary]

        :param format: [description]
        :type format: Format
        """
        return
