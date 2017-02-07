from nose.tools import *
from anagramchecker.anagramchecker import *

def test_anagramchecker():
    ana = AnagramChecker()
    assert_equal(ana.are_anagrams("eat", "tea"), True)
    assert_equal(ana.are_anagrams("spam", "eggs"), False)
