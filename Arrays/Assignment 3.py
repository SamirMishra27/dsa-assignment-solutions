from typing import List

'''
Question 1
Given an integer array nums of length n and an integer target, find three integers
in nums such that the sum is closest to the target.
Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2

Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

https://leetcode.com/problems/3sum-closest/description/
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        closest_3_nums = nums[:3]
        lowest_diff = abs(nums[0] + nums[1] + nums[2] - target)
        n = len(nums)

        if n == 3:
            return sum(nums)

        for i in range(0, n - 2):
            diff = abs(nums[i] + nums[i + 1] + nums[i + 2] - target)
            if diff < lowest_diff:
                lowest_diff = diff
                closest_3_nums = nums[i : i + 3]

        return sum(closest_3_nums)

'''
Question 2
Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:
           ● 0 <= a, b, c, d < n
           ● a, b, c, and d are distinct.
           ● nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

https://leetcode.com/problems/4sum/
'''

'''
💡 **Question 3**
A permutation of an array of integers is an arrangement of its members into a
sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr:
[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater
permutation of its integer. More formally, if all the permutations of the array are
sorted in one container according to their lexicographical order, then the next
permutation of that array is the permutation that follows it in the sorted container.

If such an arrangement is not possible, the array must be rearranged as the
lowest possible order (i.e., sorted in ascending order).

● For example, the next permutation of arr = [1,2,3] is [1,3,2].
● Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
● While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not
have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.
The replacement must be in place and use only constant extra memory.

**Example 1:**
Input: nums = [1,2,3]
Output: [1,3,2]

https://leetcode.com/problems/next-permutation/
'''
class Solution:
    def reverse(self, nums: List[int], i: int) -> None:
        i, j = i, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] < nums[i]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while nums[j] < nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        self.reverse(nums, i + 1)

'''
Question 4
Given a sorted array of distinct integers and a target value, return the index if the
target is found. If not, return the index where it would be if it were inserted in
order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

https://leetcode.com/problems/search-insert-position/
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)

        for i in range(0, n):
            if nums[i] == target or nums[i] > target:
                return i

        else:
            return n

'''
💡 **Question 5**
You are given a large integer represented as an integer array digits, where each
digits[i] is the ith digit of the integer. The digits are ordered from most significant
to least significant in left-to-right order. The large integer does not contain any
leading 0's.

Increment the large integer by one and return the resulting array of digits.

**Example 1:**
Input: digits = [1,2,3]
Output: [1,2,4]

**Explanation:** The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

https://leetcode.com/problems/plus-one/
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1

            if digits[i] == 10:
                digits[i] = 0
                if i == 0:
                    digits.insert(i, 1)
                    return digits
                continue

            return digits

'''
Question 6
Given a non-empty array of integers nums, every element appears twice except
for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only
constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

https://leetcode.com/problems/single-number/
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]

        for i in range(0, n):
            for j in range(0, n):
                if nums[i] == nums[j]:
                    break
        else:
            return nums[i]

'''
Question 7
You are given an inclusive range [lower, upper] and a sorted unique integer array
nums, where all elements are within the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in
nums.

Return the shortest sorted list of ranges that exactly covers all the missing
numbers. That is, no element of nums is included in any of the ranges, and each
missing number is covered by one of the ranges.

Example 1:
Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: [[2,2],[4,49],[51,74],[76,99]]

Explanation: The ranges are:
[2,2]
[4,49]
[51,74]
[76,99]

https://leetcode.com/problems/missing-ranges/
'''
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int):
        missing_ranges: list[list[int]] = []
        next = lower

        for i in range(0, len(nums)):
            if nums[i] < next:
                continue

            if nums[i] == next:
                next += 1
                continue

            missing_ranges.append([next, i - 1] if next != i - 1 else next)

        if next <= upper:
            missing_ranges.append([next, upper] if next != upper else next)

        return missing_ranges

'''
Question 8
Given an array of meeting time intervals where intervals[i] = [starti, endi],
determine if a person could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

https://leetcode.com/problems/meeting-rooms/
'''
class Solution:
    def canAttendAllMeetings(self, intervals: List[list]):
        intervals.sort(key = lambda x: x[0])
        for i in range(0, len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True
