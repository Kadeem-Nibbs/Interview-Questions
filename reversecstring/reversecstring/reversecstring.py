# Script Name	: reversecstring.py
# Author		: Kadeem Nibbs
# Created		: 2/5/2017
# Last Modified	:
# Version		: 1.0

# This program defines an algorithm to reverse a c-string (string terminated
# with '\0')

def reversecstring(cstr):
    listy = list(cstr[:len(cstr)-1]) # everything but terminating '\0'
    listy = listy[::-1]
    listy.append('\0')
    return "".join(listy)

# This algorithm runs in O(n) time and uses O(n) space.  Line 11 is done in
# O(n) time, 12 is done in O(n) time, 13 is done in O(1) time, and 14 is done
# in O(n) time.  At any point up to 2 additional lists using O(n) space are
# held in memory.
