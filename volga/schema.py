from volga.format import Format
from volga.protocols import supportsDeserialization


class Schema(supportsDeserialization):
    def __init__(self) -> None:
        ...

    def __deserialize__(self, format: Format) -> None:
        return
