from typing import Protocol
from serializer import Serializer
from abc import abstractmethod

class Serialize(Protocol):

    @abstractmethod
    def serialize(serializer: Serializer) -> None:
        ...
