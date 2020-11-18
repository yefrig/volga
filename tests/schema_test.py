from volga.schema import Schema
from volga.fields import Int, Float, Bool

from volga.json import deserialize
from hypothesis.core import given
from hypothesis import strategies as st

import json


class User(Schema):
    # name: Str
    age: Int
    score: Float
    verified: Bool


@given(
    a=st.integers(), s=st.floats(allow_infinity=False, allow_nan=False), v=st.booleans()
)
def test_Schema_deserialize(a: int, s: float, v: bool):
    userJSON = (
        '{"age":'
        + json.dumps(a)
        + ',"score":'
        + json.dumps(s)
        + ',"verified":'
        + json.dumps(v)
        + "}"
    )
    print(deserialize(userJSON, User), str({"age": a, "score": s, "verified": v}))

    assert str(deserialize(userJSON, User)) == str(
        User.__from_dict__({"age": a, "score": s, "verified": v})
    )

    print(deserialize(userJSON, User))
