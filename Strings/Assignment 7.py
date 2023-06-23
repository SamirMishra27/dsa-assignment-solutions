from typing import List
'''
💡 **Question 1**

Given two strings s and t, *determine if they are isomorphic*.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

**Example 1:**

**Input:** s = "egg", t = "add"

**Output:** true

https://leetcode.com/problems/isomorphic-strings/
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t))

'''
💡 **Question 2**

Given a string num which represents an integer, return true *if* num *is a **strobogrammatic number***.

A **strobogrammatic number** is a number that looks the same when rotated 180 degrees (looked at upside down).

**Example 1:**

**Input:** num = "69"

**Output:**

true

https://leetcode.com/problems/strobogrammatic-number/
'''
class Solution:
    def strobogrammatic_number(self, s: str):
        if not all(c not in s for c in '23457'):
            return False

        _s = ''
        for i in range(len(s) -1, -1, -1):
            if s[i] == '1':
                _s += '1'
            elif s[i] == '6':
                _s += '9'
            elif s[i] == '8':
                _s += '8'
            elif s[i] == '9':
                _s += '6'
            elif s[i] == '0':
                _s += '0'
        return _s == s

'''
💡 **Question 3**

Given two non-negative integers, num1 and num2 represented as string, return *the sum of* num1 *and* num2 *as a string*.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

**Example 1:**

**Input:** num1 = "11", num2 = "123"

**Output:**

"134"

https://leetcode.com/problems/add-strings/
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num2) > len(num1):
            num1, num2 = num2, num1

        carry = 0
        a = ''
        i = len(num1) - 1
        j = len(num2) - 1
        while i > -1:
            if j == -1:
                a += f'{int(num1[i]) + carry}'[-1::-1]
                carry = 0
            else:
                _a = int(num1[i]) + int(num2[j]) + carry
                a += f'{_a}'[-1]
                carry = 0
                if _a > 9:
                    carry = 1
            i -= 1
            j -= 1
        if carry:
            a += '1'
        return a[-1::-1]

'''
💡 **Question 4**

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

**Example 1:**

**Input:** s = "Let's take LeetCode contest"

**Output:** "s'teL ekat edoCteeL tsetnoc"

https://leetcode.com/problems/reverse-words-in-a-string-iii/
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        for w in range(len(s)):
            n = ''
            for i in range(len(s[w]) -1, -1, -1):
                n += s[w][i]
            s[w] = n
        return ' '.join(s)

'''
💡 **Question 5**

Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

**Example 1:**

**Input:** s = "abcdefg", k = 2

**Output:**

"bacdfeg"

https://leetcode.com/problems/reverse-string-ii/
'''
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        r = True
        a = ''
        n = len(s)
        i = 0
        if n <= k:
            return s[-1::-1]
        while i < n:
            p = s[i:i+k]
            if len(p) < k:
                a += p
                break
            if not r:
                a += p
            else:
                a += p[-1::-1]
            i += k
            r = not r
        return a

'''
💡 **Question 6**

Given two strings s and goal, return true *if and only if* s *can become* goal *after some number of **shifts** on* s.

A **shift** on s consists of moving the leftmost character of s to the rightmost position.

- For example, if s = "abcde", then it will be "bcdea" after one shift.

**Example 1:**

**Input:** s = "abcde", goal = "cdeab"

**Output:**

true

https://leetcode.com/problems/rotate-string/
'''
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for _ in range(len(s)):
            if s[1:] + s[0] == goal:
                return True
            s = s[1:] + s[0]
        return False

'''
💡 **Question 7**

Given two strings s and t, return true *if they are equal when both are typed into empty text editors*. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

**Example 1:**

**Input:** s = "ab#c", t = "ad#c"

**Output:** true

**Explanation:**

Both s and t become "ac".

https://leetcode.com/problems/backspace-string-compare/
'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s, t = s.split(), t.split()
        i = 0
        while i < len(s):
            if s[i] == '#':
                if i == 0:
                    s.remove(s[i])
                else:
                    s.remove(s[i])
                    s.remove(s[i - 1])
                    i -= 1
                    continue
            else:
                i += 1

'''
💡 **Question 8**

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

**Example 1:**
https://assets.leetcode.com/uploads/2019/10/15/untitled-diagram-2.jpg

**Input:** coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]

**Output:** true

https://leetcode.com/problems/check-if-it-is-a-straight-line/description/
'''
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if all(coordinates[0][0] == n[0] for n in coordinates):
            return True
        if all(coordinates[0][1] == n[1] for n in coordinates):
            return True
        for i in range(len(coordinates) - 1):
            if abs(coordinates[i][0] - coordinates[i + 1][0]) != abs(coordinates[i][1] - coordinates[i + 1][1]):
                return False
        return True
