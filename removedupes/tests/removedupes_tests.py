from nose.tools import *
from removedupes.removedupes import *

def test_removedupes():
    assert_equal(removedupes("abcdefg"), "abcdefg")
    assert_equal(removedupes("hello"), "helo")
    assert_equal(removedupes(""), "")
    assert_equal(removedupes("1111"), "1")

def test_removedupes2():
    x = removedupes2("abcdefg")
    y = "abcdefg"
    assert_equal(len(x), len(set(x)))
    assert_equal(set(x), set(y))

    x = removedupes2("hello")
    y = "helo"
    assert_equal(len(x), len(set(x)))
    assert_equal(set(x), set(y))

    x = removedupes2("")
    y = ""
    assert_equal(len(x), len(set(x)))
    assert_equal(set(x), set(y))

    x = removedupes2("1111")
    y = "1"
    assert_equal(len(x), len(set(x)))
    assert_equal(set(x), set(y))
    
