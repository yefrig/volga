from volga.types import supportsDeser
from volga.format import Format


class Schema(supportsDeser):
    def __deserialize__(self, format: Format) -> None:
        # will eventually deserialize Schema as a dictionary

        # hint at deserializer which type to build you from but it may
        # not listen and pass constructor that instantiates this class
        ...
