# Script Name	: removedupes.py
# Author		: Kadeem Nibbs
# Created		: 2/5/2017
# Last Modified	:
# Version		: 1.0

# This program defines a function to remove duplicate characters from a
# string without using additional data structures.

def removedupes(string):
    if not string: # stringy is empty string
        return string
    index = 0 # how far away from end of the string to look for duplicated
               # characters
    lastchar = ""
    for char in string:
        if char == lastchar:
            continue
        string = string[:index] + char + string[index+1:].replace(char, "")
        index += 1
        lastchar = char
        print index, char, string
    return string

# This algorithm runs in O(s^2) time and uses O(s) space, where s is the
# length of the input string.  This algorithm is greatly slowed down by
# the fact that strings need to be remade every time a character is deleted.
# This algorithm would be more effective when applied to a list(O(slogs)),
# but would still be suboptimal.

def removedupes2(string):
    string = "".join(set(string))
    return string

# This algorithm runs in O(s) time and uses O(s) space.  Constructing a set
# from a string is a linear speed operation and automatically removes
# duplicates.  Constructing and return a string made from the elements of
# the set is also a linear speed operation.  The only downside is that
# the original order of the characters is not conserved since sets are
# unordered.  Solution suggested on StackOverflow.


removedupes("hello")
