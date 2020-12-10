class VolgaError(Exception):
    """Base class for all volga-related errors."""

    pass


class DeserializationError(VolgaError):
    """Raised during serialization errors when parsing or building object instances."""

    pass


class ParsingError(VolgaError):
    """Raised during deserialization errors when parsing object instances."""

    pass
