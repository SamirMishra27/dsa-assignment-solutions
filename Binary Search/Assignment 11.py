from typing import List

'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

https://leetcode.com/problems/sqrtx/description/
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        if x == 1 or x == 2 or x == 3:
            return 1

        p = 2
        for i in range(2, int(x / 2) + 1):
            if i * i == x:
                return i
            if (p * p) < x < (i * i):
                break
            p = i
        return p

'''
💡 **Question 2**

A peak element is an element that is strictly greater than its neighbors.

Given a **0-indexed** integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any of the peaks**.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in `O(log n)` time.

**Example 1:**

```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

**Example 2:**
```
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
```

https://leetcode.com/problems/find-peak-element/
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        if n == 1 or nums[0] > nums[1]:
            return 0

        if nums[-1] > nums[-2]:
            return n - 1

        while l <= r:
            m = int((l + r) / 2)

            if nums[m - 1] < nums[m] > nums[m + 1]:
                return m

            if nums[m - 1] > nums[m]:
                r = m - 1

            else:
                l = m + 1
        return -1

'''
💡 **Question 3**

****

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return *the only number in the range that is missing from the array.*

**Example 1:**

```
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

```

**Example 2:**

```
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

```

**Example 3:**
```
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
```
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n not in nums:
            return n
        for i in range(n, 0, -1):
            if i - 1 not in nums:
                return i -1

'''
💡 **Question 4**

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only **one repeated number** in `nums`, return *this repeated number*.

You must solve the problem **without** modifying the array `nums` and uses only constant extra space.

**Example 1:**

```
Input: nums = [1,3,4,2,2]
Output: 2

```

**Example 2:**
```
Input: nums = [3,1,3,4,2]
Output: 3
```

https://leetcode.com/problems/find-the-duplicate-number/description/
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x, y = nums[0], nums[0]
        while nums[y] and nums[nums[y]]:
            x = nums[x]
            y = nums[nums[y]]
            if x == y:
                break
        y = nums[0]
        while y != x:
            y = nums[y]
            x = nums[x]
        return x
'''
**MOST OPTIMIZED SOLUTION ON LEETCODE**
'''

'''
💡 **Question 5**

Given two integer arrays `nums1` and `nums2`, return *an array of their intersection*. Each element in the result must be **unique** and you may return the result in **any order**.

**Example 1:**

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

```

**Example 2:**
```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
```

'''

