"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
Example 1: s = "racecar", t = "carrace" --> true
Example 2: s = "jar", t = "jam" --> false
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[s[i]] = 1 + countT.get(s[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True

s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))