from typing import List

'''
💡 **Q1.** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Example:**
Input: nums = [2,7,11,15], target = 9
Output0 [0,1]

**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1]

https://leetcode.com/problems/two-sum/
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_one: int = 0
        index_two: int = 1

        while index_one < len(nums):
            for i in range(index_two, len(nums)):
                if nums[index_one] + nums[index_two] == target:
                    index_two = i
                    return [index_one, index_two]

            index_one += 1
            index_two += 1

'''
💡 **Q2.** Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
- Return k.

**Example :**
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_*,_*]

**Explanation:** Your function should return k = 2, with the first two elements of nums being 2. It does not matter what you leave beyond the returned k (hence they are underscores)

https://leetcode.com/problems/remove-element/description/
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        skip = 0
        k = 0

        for i in range(0, len(nums)):

            while nums[i] == val or nums[i] is None:
                if nums[i] == val:
                    nums[i] = None
                    skip += 1
                    
                if i + skip >= len(nums):
                    break

                nums[i], nums[i + skip] = nums[i + skip], nums[i]

            if nums[i] != None:
                k += 1

        return k

'''
💡 **Q3.** Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

**Example 1:**
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
💡 **Q4.** You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

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
💡 **Q5.** You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

**Example 1:**
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

**Explanation:** The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

https://leetcode.com/problems/merge-sorted-array/description/
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_index = 0

        # corner cases
        if not nums1:
            return nums2
        elif not nums2:
            return nums1

        for new_elem in nums2:
            for index in range(nums1_index, m):
                if new_elem < nums1[index]:

                    nums1.insert(index, new_elem)
                    nums1_index = index

                    nums1.remove(nums1[-1])
                    nums2.remove(new_elem)
                    break

        if nums2:
            for new_elem in nums2:
                for index in range(nums1_index, m + n):
                    if nums1[index] == 0:
                        nums1[index] = new_elem
                        break

'''
💡 **Q6.** Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

**Example 1:**
Input: nums = [1,2,3,1]

Output: true

https://leetcode.com/problems/contains-duplicate/
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for x in range(0, len(nums)):
            for y in range(x + 1, len(nums)):
                if nums[x] == nums[y]:
                    return True

        return False

'''
💡 **Q7.** Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.

Note that you must do this in-place without making a copy of the array.

**Example 1:**
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

https://leetcode.com/problems/move-zeroes/
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        y = 1

        for i in range(0, len(nums)):

            if nums[i] == 0:
                for j in range(y, len(nums)):

                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        y = j
                        break

'''
💡 **Q8.** You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

**Example 1:**
Input: nums = [1,2,2,4]
Output: [2,3]

https://leetcode.com/problems/set-mismatch/
'''
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            if not nums[i] < nums[i + 1]:
                if nums[i] - 1 not in nums and nums[i] - 1 > 0:
                    return [nums[i], nums[i] - 1]
                else:
                    return [nums[i], nums[i] + 1]
