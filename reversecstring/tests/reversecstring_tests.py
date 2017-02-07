from nose.tools import *
from reversecstring.reversecstring import *

def test_reversecstring():
    cstr = "hello\x00"
    assert_equal(reversecstring(cstr), "olleh\x00")
    cstr = "\x00"
    assert_equal(reversecstring(cstr), "\x00")
