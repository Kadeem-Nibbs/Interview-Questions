from nose.tools import *
from uniquechars.uniquechars import *

def test_uniquechars():
    assert_equal(uniquechars("aa"), False)
    assert_equal(uniquechars("abcdefg"), True)
    assert_equal(uniquechars("123456"), True)
    assert_equal(uniquechars("abc123a"), False)

def test_uniquechars2():
    assert_equal(uniquechars2("aa"), False)
    assert_equal(uniquechars2("abcdefg"), True)
    assert_equal(uniquechars2("123456"), True)
    assert_equal(uniquechars2("abc123a"), False)
