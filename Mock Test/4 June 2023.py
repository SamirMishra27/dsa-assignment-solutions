# Necessary import
from typing import List

'''
Move Zeroes --- (5 POINTS)
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
a. 1 <= nums.length <= 10^4
b. -2^31 <= nums[i] <= 2^31 - 1

Note: Create a GitHub file for the solution and add the file link the the answer section below.
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        x = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[x] = nums[x], nums[i]
                x += 1
'''
Runtime: 178 ms
Memory: 17.9 MB
'''

'''
First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
a. 1 <= s.length <= 10^5
b. s consists of only lowercase English letters.

Note: Create a GitHub file for the solution and add the file link the the answer section below.
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        if s[0] not in s[1:n]:
            return 0
        for i in range(n):
            if s[i] not in s[0:i] and s[i] not in s[i+1:n]:
                return i
        if s[-1] not in s[0:n - 1]:
            return n - 1
        return -1

'''
Runtime: 131 ms
Memory: 16.5 MB

**MOST OPTIMIZED SOLUTION ON LEETCODE**
'''