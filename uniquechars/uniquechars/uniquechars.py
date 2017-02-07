# Script Name	: uniquechars.py
# Author		: Kadeem Nibbs
# Created		: 2/5/2017
# Last Modified	:
# Version		: 1.0

# This program defines a function to check if all of the characters in an
# input string are unique.  Returns True if all are unique, False
# otherwise.  The first function is for use if additional data structures
# are allowed; the second is for use if additional data structures are
# unavailable.

def uniquechars(stringy):
    dicty = {}
    for char in stringy:
        if char in dicty: # We have seen value already
            return False
        else:
            dicty[char] = 1 # Note that we have seen value
    return True

# This algorithm is completed in O(1) time and uses O(1) space.  Its runtime is bounded by
# the number of available characters (~1 million unicode, 256 ASCII). Once
# that number is surpassed, a duplicate element will be recorded.
# Pidgeonhole Principle.

def uniquechars2(stringy):
    checker = 0 # Binary number noting which characters have been seen
    for char in stringy:
        value = 1 << ord(char) # 1 in place corresponding to char
        if (checker & value > 0): # already a 1 in checker, char has been seen
            return False
        checker |= value # store 1 in checker in place corresponding to
                         # value
    return True

# Solution adapted from Cracking the Coding Interview by Gayle Laakmann
# McDowell.  Binary numbers act as two-state dictionaries where the number's
# place is the key and the value is either one or zero.  This is perfect
# for the purposes of this problem because the algorithm only runs as long
# as characters haven't occurred (0), or have only been seen once (1), and
# returns False otherwise.  The algorithm runs in
# O(1) time and uses O(1) space.  My original solutions without additional
# data structures ran in O(n^2) time and used O(n) space.
