class VolgaError(Exception):
    """Base class for all volga-related errors."""


class SerializationError(VolgaError):
    """Raised during serialization errors when parsing or building object instances."""