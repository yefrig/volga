from typing import Mapping, Sequence
from hypothesis import given
import hypothesis.strategies as st

from src.json import to_string
from src.data import VolgaT

# all tests are temporary until from_string is implemented
@given(st.integers())
def test_serialize_int(x: int):
    assert to_string(x) == str(x)


@given(st.booleans())
def test_serialize_bool(x: bool):
    assert to_string(x) == str(x).lower()


@given(st.floats())
def test_serialize_float(x: float):
    assert to_string(x) == str(x)


@given(st.text())
def test_serialize_str(x: str):
    assert to_string(x) == '"' + x + '"'

    
@given(st.none())
def test_serialize_none(x: None):
    assert to_string(x) == "null"


# test list of integers, eventually will be recursive test once from_string is implemented
@given(st.recursive(st.integers(), st.lists))
def test_serialize_seq_int(x: Sequence[VolgaT]):
    assert to_string(x) == str(x).replace(" ", "")


@given(st.recursive(st.booleans(), st.lists))
def test_serialize_seq_bool(x: Sequence[VolgaT]):
    assert to_string(x) == str(x).lower().replace(" ", "")


@given(st.recursive(st.floats(), st.lists))
def test_serialize_seq_float(x: Sequence[VolgaT]):
    assert to_string(x) == str(x).replace(" ", "")


@given(st.recursive(st.none(), st.lists))
def test_serialize_seq_none(x: Sequence[VolgaT]):
    assert to_string(x) == str(x).replace("None", "null").replace(" ", "")


@given(st.dictionaries(st.integers(), st.integers()))
def test_serialize_map_int(d: Mapping[VolgaT, VolgaT]):
    assert to_string(d) == str(d).replace(" ", "")


@given(st.dictionaries(st.booleans(), st.integers()))
def test_serialize_map_bool(d: Mapping[VolgaT, VolgaT]):
    assert to_string(d) == str(d).lower().replace(" ", "")


@given(st.dictionaries(st.floats(), st.integers()))
def test_serialize_map_float(d: Mapping[VolgaT, VolgaT]):
    assert to_string(d) == str(d).replace(" ", "")


@given(st.dictionaries(st.none(), st.integers()))
def test_serialize_map_none(d: Mapping[VolgaT, VolgaT]):
    assert to_string(d) == str(d).replace("None", "null").replace(" ", "")
