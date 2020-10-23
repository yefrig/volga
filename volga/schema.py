from abc import abstractclassmethod
from typing import Protocol
from volga.format import Format


class Constructor(Protocol):
    @abstractclassmethod
    def __from_dict__(s: str):
        ...


class Schema:
    @abstractclassmethod
    def __deserialize__(self, format: Format) -> None:
        # will eventually deserialize Schema as a dictionary

        # hint at deserializer which type to build you from but it may
        # not listen and pass constructor that instantiates this class
        ...
