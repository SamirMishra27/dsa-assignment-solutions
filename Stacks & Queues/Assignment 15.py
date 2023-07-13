from typing import List
'''
💡 **Question 1**

Given an array **arr[ ]** of size **N** having elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.Next greater element of an element in the array is the nearest element on the right which is greater than the current element.If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.

**Example 1:**

```
Input:
N = 4, arr[] = [1 3 2 4]
Output:
3 4 4 -1
Explanation:
In the array, the next larger element
to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ?
since it doesn't exist, it is -1.

```

**Example 2:**
```
Input:
N = 5, arr[] [6 8 0 1 3]
Output:
8 -1 1 3 -1
Explanation:
In the array, the next larger element to
6 is 8, for 8 there is no larger elements
hence it is -1, for 0 it is 1 , for 1 it
is 3 and then for 3 there is no larger
element on right and hence -1.
```

https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1?utm_source=gfg
'''
class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        if len(arr) == 1:
            return [-1]

        answer = []
        stack = []
        for i in range(len(arr) - 1, -1, -1):
            next_popped = arr.pop()
            while stack and next_popped >= stack[-1]:
                stack.pop()
            if not stack:
                answer.append(-1)
                stack.append(next_popped)
                continue
            else:
                answer.append(stack[-1])
                stack.append(next_popped)

        return answer[-1::-1]

'''
💡 **Question 2**

Given an array **a** of integers of length **n**, find the nearest smaller number for every element such that the smaller element is on left side.If no small element present on the left print -1.

**Example 1:**

```
Input: n = 3
a = {1, 6, 2}
Output: -1 1 1
Explaination: There is no number at the
left of 1. Smaller number than 6 and 2 is 1.
```

**Example 2:**
```
Input: n = 6
a = {1, 5, 0, 3, 4, 5}
Output: -1 1 -1 0 3 4
Explaination: Upto 3 it is easy to see
the smaller numbers. But for 4 the smaller
numbers are 1, 0 and 3. But among them 3
is closest. Similary for 5 it is 4.
```

https://practice.geeksforgeeks.org/problems/smallest-number-on-left3403/1?utm_source=gfg
'''
class Solution:
    def leftSmaller(self, n, arr):
        # code here
        if len(arr) == 1:
            return [-1]

        answer = []
        stack = []
        arr.reverse()
        for i in range(len(arr) - 1, -1, -1):
            next_popped = arr.pop()
            while stack and stack[-1] >= next_popped:
                stack.pop()
            if not stack:
                answer.append(-1)
                stack.append(next_popped)
                continue
            else:
                answer.append(stack[-1])
                stack.append(next_popped)

        return answer

'''
💡 **Question 3**

Implement a Stack using two queues **q1** and **q2**.

**Example 1:**

```
Input:
push(2)
push(3)
pop()
push(4)
pop()
Output:3 4
Explanation:
push(2) the stack will be {2}
push(3) the stack will be {2 3}
pop()   poped element will be 3 the
        stack will be {2}
push(4) the stack will be {2 4}
pop()   poped element will be 4

```

**Example 2:**
```
Input:
push(2)
pop()
pop()
push(3)
Output:2 -1
```

https://practice.geeksforgeeks.org/problems/stack-using-two-queues/1?
'''
#Function to push an element into stack using two queues.
def push(x):

    # global declaration
    global queue_1
    global queue_2

    # code here
    queue_2.insert(0, x)
    while queue_1:
        queue_2.insert(0, queue_1.pop())
    queue_1, queue_2 = queue_2, queue_1
    # queue_2.append(x)


#Function to pop an element from stack using two queues.
def pop():

    # global declaration
    global queue_1
    global queue_2

    # code here
    if not queue_1:
        return -1
    return queue_1.pop()

'''
💡 **Question 4**

You are given a stack **St**. You have to reverse the stack using recursion.

**Example 1:**

```
Input:St = {3,2,1,7,6}
Output:{6,7,1,2,3}
```

**Example 2:**
```
Input:St = {4,3,9,6}
Output:{6,9,3,4}
```

https://practice.geeksforgeeks.org/problems/reverse-a-stack/1?utm_source=gfg
'''
class Solution:
    def reverse(self, St: 'list[int]'):
        #code here
        if len(St) == 1:
            return St #[1]

        elem = [St.pop()]
        St = self.reverse(St)
        elem.extend(St)
        return St

'''
💡 **Question 5**

You are given a string **S**, the task is to reverse the string using stack.

**Example 1:**
```
Input: S="GeeksforGeeks"
Output: skeeGrofskeeG
```

https://practice.geeksforgeeks.org/problems/reverse-a-string-using-stack/1
'''
def reverse(S):

    #Add code here
    s = []
    while S:
        s.append(S[0])
        S = S[1:]

    while s:
        S += s.pop()
    return S

'''
💡 **Question 6**

Given string **S** representing a postfix expression, the task is to evaluate the expression and find the final value. Operators will only include the basic arithmetic operators like ***, /, + and -**.

**Example 1:**

```
Input: S = "231*+9-"
Output: -4
Explanation:
After solving the given expression,
we have -4 as result.

```

**Example 2:**
```
Input: S = "123+*8-"
Output: -3
Explanation:
After solving the given postfix
expression, we have -3 as result.
```

https://practice.geeksforgeeks.org/problems/evaluation-of-postfix-expression1735/1
'''
class Solution:
    
    #Function to evaluate a postfix expression.
    def evaluatePostfix(self, S):
        #code here
        stack = []
        for i in range(len(S)):
            if S[i].isnumeric():
                stack.append(S[i])
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(eval(f'{a}{S[i]}{b}'))
        return -stack[0]

'''
💡 **Question 7**

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

**Example 1:**
```
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

https://leetcode.com/problems/min-stack/
'''


'''
💡 **Question 8**

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

Example 1:
https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

Example 2:
```
Input: height = [4,2,0,3,2,5]
Output: 9
```

https://leetcode.com/problems/trapping-rain-water/
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0

        rainwater = 0
        stack = []
        highest_n_index = height.index(max(height))
        for i in range(len(height) -1, -1, -1):
            if height[i] == height[highest_n_index]:
                highest_n_index = i
                break
        for n in range(len(height) ):
            while stack and stack[-1] < height[n]:
                p = stack.pop()
                if n > highest_n_index:
                    rainwater += height[n] - p
            if not stack:
                stack.append(height[n])
                continue
            if not n > highest_n_index:
                rainwater += stack[0] - height[n]
            stack.append(height[n])
        return rainwater

