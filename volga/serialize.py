from typing import Protocol
from volga import Serializer
from abc import abstractmethod

class Serialize(Protocol):

    @abstractmethod
    def serialize(serializer: Serializer) -> None:
        ...
