import pytest

@pytest.fixture(scope="function")
def mathstr1():
    return MathStr("a")

@pytest.fixture(scope="function")
def mathstr2():
    return MathStr("abc")

@pytest.fixture(scope="function")
def mathstr3():
    return MathStr("abcdef")


# Binary operator tests

def test_str_addition(mathstr1):
    assert mathstr1 + "abc" == MathStr("aabc")

def test_str_subtraction(mathstr1, mathstr2, mathstr2):
    assert MathStr("abc") - "c" == MathStr("ab")
    assert MathStr("aabc") - "abc" == mathstr1
    assert mathstr2 - mathstr1 + mathstr1 == mathstr2
    assert mathstr2 - mathstr1 == MathStr(["a", "b", "c", -MathStr("a")])

    assert mathstr3 - mathstr2 == MathStr(["abcdef", -MathStr("abc")])
    assert mathstr3 - mathstr2 + mathstr2 == mathstr3


# Unary operator tests

def test_str_negation(mathstr2):
    assert -mathstr2 == MathStr([-MathStr("a"), -MathStr("b"), -MathStr("c")])
    assert -(-mathstr2) == mathstr2
