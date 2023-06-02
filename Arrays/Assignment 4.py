from typing import List

'''
💡 **Question 1**
Given three integer arrays arr1, arr2 and arr3 **sorted** in **strictly increasing** order, return a sorted array of **only** the integers that appeared in **all** three arrays.

**Example 1:**

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]

Output: [1,5]

**Explanation:** Only 1 and 5 appeared in the three arrays.

https://leetcode.com/problems/intersection-of-three-sorted-arrays/
'''
class Solution:
    def check_array(self, arr: List[int], nums: dict):
        for num in arr:
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1
        
    def arrays_intersection(self, arr1: List[int], arr2: List[int], arr3: List[int]):

        nums = {}
        if arr1:
            self.check_array(arr1, nums)

        if arr2:
            self.check_array(arr2, nums)

        if arr3:
            self.check_array(arr3, nums)

        return list([num for num, count in nums.items() if count == 3])

'''
💡 **Question 2**

Given two **0-indexed** integer arrays nums1 and nums2, return *a list* answer *of size* 2 *where:*

- answer[0] *is a list of all **distinct** integers in* nums1 *which are **not** present in* nums2*.*
- answer[1] *is a list of all **distinct** integers in* nums2 *which are **not** present in* nums1.

**Note** that the integers in the lists may be returned in **any** order.

**Example 1:**

**Input:** nums1 = [1,2,3], nums2 = [2,4,6]

**Output:** [[1,3],[4,6]]

**Explanation:**

For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].

For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

https://leetcode.com/problems/find-the-difference-of-two-arrays/description/
'''
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_len = len(nums1)
        nums2_len = len(nums2)

        distinct_nums_nums1 = set()
        distinct_nums_nums2 = set()

        for i in range( 0, max(nums1_len, nums2_len) ):
            if i < nums1_len:
                if nums1[i] not in nums2:
                    distinct_nums_nums1.add(nums1[i])

            if i < nums2_len:
                if nums2[i] not in nums1:
                    distinct_nums_nums2.add(nums2[i])

        return [distinct_nums_nums1, distinct_nums_nums2]

'''
💡 **Question 3**
Given a 2D integer array matrix, return *the **transpose** of* matrix.

The **transpose** of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

**Example 1:**

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]

Output: [[1,4,7],[2,5,8],[3,6,9]]

https://leetcode.com/problems/transpose-matrix/
'''
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        x, j = 0, 0
        length = len(matrix)

        while x < length:
            while j < length:
                if x != j:
                    matrix[j][x], matrix[x][j] = matrix[x][j], matrix[j][x]
                j += 1
            x += 1
            j = x

        return matrix

'''
💡 Question 4
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
💡 **Question 5**
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase **may be** incomplete.

Given the integer n, return *the number of **complete rows** of the staircase you will build*.

**Example 1:**

[]()

![v2.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4bd91cfa-d2b1-47b3-8197-a72e8dcfff4b/v2.jpg)

**Input:** n = 5

**Output:** 2

**Explanation:** Because the 3rd row is incomplete, we return 2.

https://leetcode.com/problems/arranging-coins/
'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 1
        while n > 0:
            if n - count < 0:
                break
            n -= count
            count += 1
        return count - 1

'''
💡 **Question 6**
Given an integer array nums sorted in **non-decreasing** order, return *an array of **the squares of each number** sorted in non-decreasing order*.

**Example 1:**

Input: nums = [-4,-1,0,3,10]

Output: [0,1,9,16,100]

**Explanation:** After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100]

https://leetcode.com/problems/squares-of-a-sorted-array/
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)
        while nums[0] < 0:

            num = nums[0]
            for j in range(n - 1, -1, -1):
                if nums[j] <= abs(num):

                    nums.remove(num)
                    if j == n - 1:
                        nums.append(abs(num))
                    else:
                        nums.insert(j, abs(num))
                    break

        for i in range(0, n):
            nums[i] = nums[i] ** 2
        return nums

'''
💡 **Question 7**
You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return *the number of maximum integers in the matrix after performing all the operations*

**Example 1:**

![q4.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4d0890d0-7bc7-4f59-be8e-352d9f3c1c52/q4.jpg)

**Input:** m = 3, n = 3, ops = [[2,2],[3,3]]

**Output:** 4

**Explanation:** The maximum integer in M is 2, and there are four of it in M. So return 4.

https://leetcode.com/problems/range-addition-ii/description/
'''

'''
💡 **Question 8**

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

*Return the array in the form* [x1,y1,x2,y2,...,xn,yn].

**Example 1:**

**Input:** nums = [2,5,1,3,4,7], n = 3

**Output:** [2,3,5,4,1,7]

**Explanation:** Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

https://leetcode.com/problems/shuffle-the-array/
'''
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if n == 1:
            return nums

        i = 0
        n2 = n*2
        while i < n2:
            if i == n2 - 2 or i + n > n2 - 1:
                break
            num = nums[i + n]
            nums.remove(num)
            nums.insert(i + 1, num)
            i += 2
        return nums
