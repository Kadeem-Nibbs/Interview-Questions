# Script Name	: reversecstring.py
# Author		: Kadeem Nibbs
# Created		: 2/5/2017
# Last Modified	:
# Version		: 1.0

class AnagramChecker(object):

    def are_anagrams(self,str1, str2):
        if len(str1) != len(str2):
            return False
        dict1 = {}
        dict2 = {}
        for char in str1:
            if char not in dict1:
                dict1[char] = 1
            else:
                dict1[char] += 1
        for char in str2:
            if char not in dict1:
                return False
            if char not in dict2:
                dict2[char] = 1
            else:
                dict2[char] += 1
        for key in dict1:
            if dict1[key] != dict2[key]:
                return False
        return True

# This algorithm runs in O(s1 + s2) time where s1 and s2 are the lengths of
# str1 and str2 respectively the function uses O(s1 + s2) space between the
# two dictionaries.  Each dictionary operation is performed in constant time
# assuming no name collision between the hashes of the keys, and the len
# operation takes constant time as well.  Each string is traversed a maximum
# of twice with each item being visited only once per traversal.
