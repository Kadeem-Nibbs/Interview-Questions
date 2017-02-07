from nose.tools import *
from spacereplace.spacereplace import *

def test_spacereplace():
    assert_equal(spacereplace("Hello World"), "Hello%20World")
    assert_equal(spacereplace("spam"), "spam")
    assert_equal(spacereplace("  "), "%20%20")
