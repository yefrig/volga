from volga.fields import Bool, Float, Int, Null, Str, Dict

# TODO: use hypothesis for these tests once classes are more robust
def test_Bool_repr():
    assert str(Bool(True)) == str(True)
    assert str(Bool(0)) == str(False)


def test_Bool_build_from_bool():
    assert Bool.__from_bool__(True) == True


def test_Bool_build_from_int():
    assert Bool.__from_int__(1) == True


def test_Bool_build_from_float():
    assert Bool.__from_float__(1.0) == True


def test_Int_build_from_bool():
    assert Int.__from_bool__(True) == 1


def test_Int_build_from_int():
    assert Int.__from_int__(1) == 1


def test_Int_build_from_float():
    assert Int.__from_float__(1.0) == 1


def test_Int_build_from_str():
    assert Int.__from_str__("1") == 1


def test_Float_build_from_bool():
    assert Float.__from_bool__(True) == 1


def test_Float_build_from_int():
    assert Float.__from_int__(1) == 1


def test_Float_build_from_float():
    assert Float.__from_float__(1.0) == 1


def test_Float_build_from_str():
    assert Float.__from_str__("1.0") == 1


def test_Str_build_from_bool():
    assert Str.__from_bool__(True) == "True"


def test_Str_build_from_int():
    assert Str.__from_int__(1) == "1"


def test_Str_build_from_float():
    assert Str.__from_float__(1.0) == "1.0"


def test_Str_build_from_str():
    assert Str.__from_str__("1.0") == "1.0"


def test_Str_build_from_None():
    assert Str.__from_none__(None) == "None"


def test_Str_build_from_dict():
    assert Str.__from_dict__({}) == "{}"


def test_Null_repr():
    assert str(Null(None)) == str(None)


def test_Null_call():
    assert Null(None).__call__() == None


def test_Null_nonzero():
    assert Null(None).__nonzero__() == 0


def test_Null_build_from_None():
    assert Null.__from_none__(None) == None


def test_Dict_build_from_Dict():
    assert Dict.__from_dict__({"a": 1}) == {"a": 1}
