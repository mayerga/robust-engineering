"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1: strs = ["act","pots","tops","cat","stop","hat"] --> [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2: strs = ["x"] --> [["x"]]
Example 3: strs = [""] --> [[""]]
"""
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        my_dict = defaultdict(list)
        print(my_dict)

        for s in strs:
            my_dict = sorted(s)
            print(my_dict)

        return []



s = Solution()
print(s.groupAnagrams(["act","pots","tops","cat","stop","hat"]))