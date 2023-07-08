from typing import List
'''
💡 **Question 1**

Given two strings s1 and s2, return *the lowest **ASCII** sum of deleted characters to make two strings equal*.

**Example 1:**

**Input:** s1 = "sea", s2 = "eat"

**Output:** 231

**Explanation:** Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.

Deleting "t" from "eat" adds 116 to the sum.

At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
'''

'''
💡 **Question 2**

Given a string s containing only three types of characters: '(', ')' and '*', return true *if* s *is **valid***.

The following rules define a **valid** string:

- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

**Example 1:**

**Input:** s = "()"

**Output:**

true

https://leetcode.com/problems/valid-parenthesis-string/
'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        if len(s) == 1:
            return True if s == '*' else False

        i, n = 0, len(s)
        while i < n:
            j = n - i - 1

            if i >= j:
                if i > j or (i == j and s[i] == '*'):
                    break
                else:
                    return False

            if (
                (s[i] == '(' and s[j] == ')') or
                (s[i] == '*' and s[j] == ')') or
                (s[i] == '(' and s[j] == '*')
            ):
                i += 1
                continue

            else:
                return False

        return True

'''
💡 **Question 3**

Given two strings word1 and word2, return *the minimum number of **steps** required to make* word1 *and* word2 *the same*.

In one **step**, you can delete exactly one character in either string.

**Example 1:**

**Input:** word1 = "sea", word2 = "eat"

**Output:** 2

**Explanation:** You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

https://leetcode.com/problems/delete-operation-for-two-strings/
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word2 in word1:
            return len(word1) - len(word2)

        if word1 in word2:
            return len(word2) - len(word1)

        if len(word2) > len(word1):
            word2, word1 = word1, word2

        common_substring_l = ''
        common_substring = ''
        i, j = 0, 0

        while i < len(word1):
            if j >= len(word2):
                break

            if word1[i] == word2[j]:
                common_substring += word1[i]
                i += 1
                j += 1

            else:
                j = 0
                if len(common_substring) > len(common_substring_l):
                    common_substring_l = common_substring
                common_substring = ''

        return (len(word1) - len(common_substring)) + (len(word2) - len(common_substring))

'''
💡 **Question 4**

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.
You always start to construct the **left** child node of the parent first if it exists.

https://practice.geeksforgeeks.org/problems/construct-binary-tree-from-string-with-bracket-representation/1
'''

'''
💡 **Question 5**

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of **consecutive repeating characters** in chars:

- If the group's length is 1, append the character to s.
- Otherwise, append the character followed by the group's length.

The compressed string s **should not be returned separately**, but instead, be stored **in the input character array chars**. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done **modifying the input array,** return *the new length of the array*.

You must write an algorithm that uses only constant extra space.

**Example 1:**

**Input:** chars = ["a","a","b","b","c","c","c"]

**Output:** Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

**Explanation:**

The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

https://leetcode.com/problems/string-compression/description/
'''
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        i = 0
        cl = 1
        while i < len(chars):
            if i + 1 >= len(chars):
                if cl > 1:
                    for c in str(cl):
                        chars.append(c)
                break
            if chars[i] == chars[i + 1]:
                del chars[i + 1]
                cl += 1
                continue

            elif chars[i] != chars[i + 1]:
                if cl == 1:
                    i += 1
                    continue
                else:
                    for c in str(cl)[-1::-1]:
                        chars.insert(i + 1, c)
                    i += 1 + len(str(cl))
                    cl = 1
                    continue
        return len(chars)

'''
💡 **Question 6**

Given two strings s and p, return *an array of all the start indices of* p*'s anagrams in* s. You may return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**

**Input:** s = "cbaebabacd", p = "abc"

**Output:** [0,6]

**Explanation:**

The substring with start index = 0 is "cba", which is an anagram of "abc".

The substring with start index = 6 is "bac", which is an anagram of "abc".

https://leetcode.com/problems/find-all-anagrams-in-a-string/
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indices = []
        p = sorted(p)

        i, n = 0, len(p)
        while i < len(s):
            if sorted(s[i: i + n]) == p:
                indices.append(i)
            i += 1
        return indices

'''
💡 **Question 7**

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

**Example 1:**

**Input:** s = "3[a]2[bc]"

**Output:** "aaabcbc"

https://leetcode.com/problems/decode-string/
'''
class Solution:
    def decodeString(self, s: str) -> str:
        curr = s[0]
        to_add = ''
        final = ''
        i = 0

        for c in s:
            if c.isnumeric():
                break
            final += c
            i += 1
        if i == len(s):
            return s
        # i = 0
        num = ''

        while i < len(s):
            if s[i].isnumeric():
                num += s[i]
                i += 1
            elif s[i] == '[':
                curr = int(num) if num else 1
                j = i + 1
                depth = 1
                stack = ['[']
                while stack:
                    if s[j] == ']':
                        stack.pop()
                    elif s[j] == '[':
                        depth += 1
                        stack.append('[')
                    else:
                        to_add += s[j]
                    j += 1
                if depth > 1:
                    final += self.decodeString(s[i + 1: j - 1]) * curr
                else:
                    final += curr * to_add
                i += j - i # 1
                to_add = ''
                num = ''
            else:
                if not s[i].isnumeric():
                    final += s[i]
                i += 1

        # to_add = ''
        # for c in s[-1::-1]:
        #     if c == ']':
        #         break
        #     to_add = c + to_add
        # final = final + to_add
        return final

'''
💡 **Question 8**

Given two strings s and goal, return true *if you can swap two letters in* s *so the result is equal to* goal*, otherwise, return* false*.*

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

- For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

**Example 1:**

**Input:** s = "ab", goal = "ba"

**Output:** true

**Explanation:** You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

https://leetcode.com/problems/buddy-strings/description/
'''
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal and s[-1::-1] == goal:
            return True

        if len(s) == 2:
            return s[-1::-1] == goal

        indexes = []
        unequal = False
        i = 0
        while i < len(s):
            if not s[i] == goal[i]:
                unequal = True
                indexes.append(i)
                if len(indexes) >= 2:
                    x, y = indexes[0], indexes[1]
                    if s[x] == goal[y] and s[y] == goal[x] and s[y+1:] == goal [y+1:]:
                        return True
            i += 1
        if not unequal and s[-1::-1] == goal:
            return True
        return False
