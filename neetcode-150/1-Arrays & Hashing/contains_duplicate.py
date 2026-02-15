"""
Give an integer array nums, return if any value appears more than once in the array, otherwise return false.
Example 1: nums = [1, 2, 3, 3] ---> true
Example 2: nums = [1, 2, 3, 4] ---> false

"""

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:

        hashSet = set()
        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
        return False

nums = [1, 2, 3, 3]
s = Solution()
print(s.hasDuplicate(nums))

