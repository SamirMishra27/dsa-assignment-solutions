from typing import List

'''
💡 **Question 1**
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2),..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

**Example 1:**
Input: nums = [1,4,3,2]
Output: 4

**Explanation:** All possible pairings (ignoring the ordering of elements) are:

1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4

https://leetcode.com/problems/array-partition/
'''
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        max_sum = 0

        n = int(len(nums) / 2)
        for i in range(0, n):
            max_sum += min(nums[i + i], nums[i + i + 1])

        return max_sum

'''
Question 2
Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor. 

The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice. 

Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.

Example 1:
Input: candyType = [1,1,2,2,3,3]
Output: 3

Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.

https://leetcode.com/problems/distribute-candies/
'''
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        prev_candy = None
        unique_candies: int = 0

        n = int(len(candyType) / 2)
        for candy in candyType:
            if candy != prev_candy:
                prev_candy = candy
                unique_candies += 1

        if unique_candies > n:
            return n
        return unique_candies

'''
Question 3
We define a harmonious array as an array where the difference between its maximum value
and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence
among all its possible subsequences.

A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5

Explanation: The longest harmonious subsequence is [3,2,2,2,3].

https://leetcode.com/problems/longest-harmonious-subsequence/description/
'''
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        starting_num: int = nums[0]
        lowest_diff: int = abs(nums[0] - nums[1])
        max_len = len(nums)

        for i in range(1, max_len):

            if i + 1 == max_len:
                return max_len

            diff = abs(nums[i] - nums[i + 1])

            if diff > lowest_diff or abs(nums[i + 1] - starting_num) > lowest_diff:
                nums.remove(nums[i + 1])
                max_len -= 1

            elif diff < lowest_diff:
                diff = lowest_diff
                nums.remove(starting_num)

                starting_num = nums[0]
                max_len -= 1

'''
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

https://leetcode.com/problems/can-place-flowers/
'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        can_plant = 0

        if not n:
            return True

        if len(flowerbed) == 1:
            return True if not flowerbed[0] and n == 1 else False
        
        skip_next_index = False
        for i in range(1, len(flowerbed) - 1):
            if skip_next_index:
                skip_next_index = False
                continue

            if 0 == flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1]:
                can_plant += 1
                skip_next_index = True

        if flowerbed[0] == flowerbed[1] == 0:
            can_plant += 1

        if flowerbed[-1] == flowerbed[-2] == 0:
            can_plant += 1

        return True if can_plant >= n else False

'''
Question 5
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:
Input: nums = [1,2,3]
Output: 6

https://leetcode.com/problems/maximum-product-of-three-numbers/
'''
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        high1 = -1000
        high2 = -999
        high3 = -998

        for num in nums:
            if num > high1:
                high3 = high2
                high2 = high1
                high1 = num

            elif high1 > num > high2:
                high3 = high2
                high2 = num

            elif high2 > num > high3:
                high3 = num

        return high1 * high2 * high3

'''
Question 6
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise,
return -1.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Explanation: 9 exists in nums and its index is 4

https://leetcode.com/problems/binary-search/description/
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        mid_num = int(len(nums) / 2)
        n = len(nums)

        if target == nums[mid_num]:
            return mid_num

        elif target > nums[mid_num]:
            for i in range(mid_num, n):
                if nums[i] == target:
                    return i
            else:
                return -1

        else:
            for i in range(mid_num, -1, -1):
                if nums[i] == target:
                    return i
            else:
                return -1

'''
Question 7
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is
monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Example 1:
Input: nums = [1,2,2,3]
Output: true

https://leetcode.com/problems/monotonic-array/description/
'''
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        i, j = None, None
        n = len(nums)
        if n <= 2:
            return True

        for i in range(0, n - 1):
            if nums[i] != nums[i + 1]:
                i, j = i, i + 1
                break
        else:
            return True

        # Monotone decreasing
        if nums[i] > nums[j]:
            prev_num: int = 10 ** 5

            for num in nums:
                if num <= prev_num:
                    prev_num = num
                    continue
                else:
                    return False

        # Monotone increasing
        elif nums[i] < nums[j]:
            prev_num: int = -10 ** 5

            for num in nums:
                if num >= prev_num:
                    prev_num = num
                    continue
                else:
                    return False
        return True

'''
Question 8
You are given an integer array nums and an integer k.

In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i] to nums[i] + x where x is an integer from the range [-k, k]. You can apply this operation at most once for each index i.

The score of nums is the difference between the maximum and minimum elements in nums.

Return the minimum score of nums after applying the mentioned operation at most once for each index in it.

Example 1:
Input: nums = [1], k = 0
Output: 0

Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.

https://leetcode.com/problems/smallest-range-i/
'''
class Solution:
    def reduceDiff(self, nums: List[int], i: int, j: int, k: int) -> None:
        diff = abs(nums[i] - nums[j])

        if diff == 0:
            return

        elif diff > k:
            diff = k

        if nums[i] > nums[j]:
            nums[i] -= diff

        elif nums[i] < nums[j]:
            nums[i] += diff

    def smallestRangeI(self, nums: List[int], k: int) -> int:

        n = len(nums)
        if n == 1:
            return 0

        self.reduceDiff(nums, 0, 1, k)

        for i in range(1, n):
            self.reduceDiff(nums, i, i - 1, k)

        return max(nums) - min(nums)
