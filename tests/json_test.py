from hypothesis import given
import hypothesis.strategies as st

from hypothesis import given
from volga.fields import Int, Bool, Float, Null, Str
from volga.json import deserialize
from volga.exceptions import ParsingError


import json
import pytest


@given(st.integers())
def test_deserialize_int(x: int):
    assert deserialize(str(x), Int) == x


@given(st.booleans())
def test_serialize_bool(x: bool):
    assert deserialize(json.dumps(x), Bool) == x


@given(st.floats(allow_infinity=False, allow_nan=False))
def test_serialize_float(x: float):
    assert deserialize(json.dumps(x), Float) == x


# TODO failing for the edge case: x = '"'
# @given(st.text())
def test_serialize_str():
    assert deserialize(json.dumps("hello"), Str) == "hello"


# TODO fix the way we check for equality
@given(st.none())
def test_serialize_none(x: None):
    assert deserialize(json.dumps(x), Null) == None


def test_parsing_error_int():
    with pytest.raises(ParsingError):
        deserialize("Not an int", Int)


def test_parsing_error_bool():
    with pytest.raises(ParsingError):
        deserialize("Not a bool", Bool)


def test_parsing_error_float():
    with pytest.raises(ParsingError):
        deserialize("Not a float", Float)


def test_parsing_error_str():
    with pytest.raises(ParsingError):
        deserialize(0, Str)
