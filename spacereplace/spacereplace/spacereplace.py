# Script Name	: spacereplace.py
# Author		: Kadeem Nibbs
# Created		: 2/5/2017
# Last Modified	:
# Version		: 1.0

# This program defines a function to remove duplicate characters from a
# string without using additional data structures.

def spacereplace(stringy):
    spacesremoved = stringy.split(" ")
    spacesreplaced = "%20".join(spacesremoved)
    return spacesreplaced
