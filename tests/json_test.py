from typing import Mapping, Sequence
from hypothesis import given
import hypothesis.strategies as st

from hypothesis import given
from volga.fields import Int, Bool, Float, Str, Null, Dict
from volga.json import deserialize
from volga.schema import Schema

import json


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
# def test_serialize_str(x: str):
#     assert deserialize(json.dumps(x), Str) == x

# TODO fix the way we check for equality
@given(st.none())
def test_serialize_none(x: None):
    assert deserialize(json.dumps(x), Null) == None


# class User(Schema):
#     # name: Str
#     age: Int
#     score: Float
#     verified: Bool


# @given(
#     a=st.integers(), s=st.floats(allow_infinity=False, allow_nan=False), v=st.booleans()
# )
# def test_deserialize_user(a: int, s: float, v: bool):
#     userJSON = (
#         '{"age":'
#         + json.dumps(a)
#         + ',"score":'
#         + json.dumps(s)
#         + ',"verified":'
#         + json.dumps(v)
#         + "}"
#     )
#     assert deserialize(userJSON, User) == User(age=a, score=s, verified=v)
