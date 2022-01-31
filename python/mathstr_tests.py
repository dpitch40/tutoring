import pytest

@pytest.fixture(scope="function")
def mathstr1():
    return MathStr("a")

@pytest.fixture(scope="function")
def mathstr2():
    return MathStr("abc")


# Binary operator tests

def test_int_addition(mathstr2):
    assert mathstr2 + 1 == 

def test_str_addition(mathstr2):
    assert mathstr2 + "abc" == MathStr("aabc")
