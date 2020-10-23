from abc import abstractclassmethod
from typing import Protocol
from volga.fields import Field
from volga.format import Format


class Constructor(Protocol):
    @abstractclassmethod
    def __from_dict__(s: str):
        ...


class SchemaMeta(type):
    def __new__(cls, name, bases, attrs):

        # Fields declared directly on the class.
        d_fields = {}

        # Take all the Fields from the attributes.
        for attr_name, field in attrs.items():
            if isinstance(field, Field):
                d_fields[attr_name] = field
        for k in d_fields.keys():
            del attrs[k]

        new_cls = super(SchemaMeta, cls).__new__(cls, name, bases, attrs)

        new_cls._d_fields = d_fields
        return new_cls


class Schema(metaclass=SchemaMeta):
    @abstractclassmethod
    def __deserialize__(self, format: Format) -> None:
        # will eventually deserialize Schema as a dictionary

        # hint at deserializer which type to build you from but it may
        # not listen and pass constructor that instantiates this class
        ...
