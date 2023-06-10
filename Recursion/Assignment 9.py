from typing import List

'''
💡 **Question 1**

Given an integer `n`, return *`true` if it is a power of two. Otherwise, return `false`*.

An integer `n` is a power of two, if there exists an integer `x` such that `n == 2x`.

**Example 1:**
Input: n = 1 

Output: true

**Example 2:**
Input: n = 16 

Output: true

**Example 3:**
Input: n = 3 

Output: false

https://leetcode.com/problems/power-of-two/description/
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:
            return False

        elif n == 1:
            return True

        if n % 2 == 0:
            return self.isPowerOfTwo(n / 2)

'''
💡 **Question 2**

Given a number n, find the sum of the first natural numbers.

**Example 1:**

Input: n = 3 

Output: 6

**Example 2:**

Input  : 5 

Output : 15

Question not found on leetcode
'''
class Solution:
    def findSum(self, n: int):

        if n == 1 or n == 0:
            return n
        
        return n + self.findSum(n - 1)

'''
💡 **Question 3**

****Given a positive integer, N. Find the factorial of N. 

**Example 1:**

Input: N = 5 

Output: 120

**Example 2:**

Input: N = 4

Output: 24

Question not found on leetcode
'''
class Solution:
    def factorialOfN(self, n: int):

        if n == 1:
            return 1

        return n * self.factorialOfN(n - 1)

'''
💡 **Question 4**

Given a number N and a power P, the task is to find the exponent of this number raised to the given power, i.e. N^P.

**Example 1 :** 

Input: N = 5, P = 2

Output: 25

**Example 2 :**
Input: N = 2, P = 5

Output: 32

Question not found on leetcode
'''
class Solution:
    def powerOfN(self, n: int, p: int):
        if p == 1:
            return n
        return n * self.powerOfN(n, p - 1)

'''
💡 **Question 5**

Given an array of integers **arr**, the task is to find maximum element of that array using recursion.

**Example 1:**

Input: arr = {1, 4, 3, -5, -4, 8, 6};
Output: 8

**Example 2:**

Input: arr = {1, 4, 45, 6, 10, -8};
Output: 45

Question not found on leetcode
'''
class Solution:
    def maxElemArray(self, arr: List[int]):
        if len(arr) == 1:
            return arr[0]
        
        if arr[0] >= arr[1]:
            arr.remove(arr[1])
        else:
            arr.remove(arr[0])
        
        return self.maxElemArray(arr=arr)

'''
💡 **Question 6**

Given first term (a), common difference (d) and a integer N of the Arithmetic Progression series, the task is to find Nth term of the series.

**Example 1:**

Input : a = 2 d = 1 N = 5
Output : 6
The 5th term of the series is : 6

**Example 2:**

Input : a = 5 d = 2 N = 10
Output : 23
The 10th term of the series is : 23

Question not found on leetcode

https://www.geeksforgeeks.org/program-n-th-term-arithmetic-progression-series/
'''
class Solution:
    def findNArithmetic(self, a: int, d: int, n: int):
        if n == 1:
            return a
        
        return self.findNArithmetic(a + d, d, n - 1)

'''
💡 **Question 7**

Given a string S, the task is to write a program to print all permutations of a given string.

**Example 1:**

***Input:***

*S = “ABC”*

***Output:***

*“ABC”, “ACB”, “BAC”, “BCA”, “CBA”, “CAB”*

**Example 2:**

***Input:***

*S = “XY”*

***Output:***

*“XY”, “YX”*

https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
'''
class Solution:
    def permutationsArray(self, arr: List[int], x: int, y: int):
        if x == y:
            print(''.join(arr))

        for i in range(x, y):
            arr[y], arr[i] = arr[i], arr[y]
            self.permutationsArray(arr, x + 1, y)
            arr[y], arr[i] = arr[i], arr[y]

'''
💡 **Question 8**

Given an array, find a product of all array elements.

**Example 1:**

Input  : arr[] = {1, 2, 3, 4, 5}
Output : 120
**Example 2:**

Input  : arr[] = {1, 6, 3}
Output : 18

https://www.geeksforgeeks.org/program-for-product-of-array/
'''
class Solution:
    def productOfAnArray(self, arr: List[int]):
        sum = arr[0]

        for i in range(len(arr)):
            sum *= arr[i]
        return sum
