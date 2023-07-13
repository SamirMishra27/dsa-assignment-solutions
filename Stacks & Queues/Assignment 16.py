'''
💡 **Question 1**

Given an array, for each element find the value of the nearest element to the right which is having a frequency greater than that of the current element. If there does not exist an answer for a position, then make the value ‘-1’.

**Examples:**

```
Input: a[] = [1, 1, 2, 3, 4, 2, 1]
Output : [-1, -1, 1, 2, 2, 1, -1]

Explanation:
Given array a[] = [1, 1, 2, 3, 4, 2, 1]
Frequency of each element is: 3, 3, 2, 1, 1, 2, 3

Lets calls Next Greater Frequency element as NGF
1. For element a[0] = 1 which has a frequency = 3,
   As it has frequency of 3 and no other next element
   has frequency more than 3 so  '-1'
2. For element a[1] = 1 it will be -1 same logic
   like a[0]
3. For element a[2] = 2 which has frequency = 2,
   NGF element is 1 at position = 6  with frequency
   of 3 > 2
4. For element a[3] = 3 which has frequency = 1,
   NGF element is 2 at position = 5 with frequency
   of 2 > 1
5. For element a[4] = 4 which has frequency = 1,
   NGF element is 2 at position = 5 with frequency
   of 2 > 1
6. For element a[5] = 2 which has frequency = 2,
   NGF element is 1 at position = 6 with frequency
   of 3 > 2
7. For element a[6] = 1 there is no element to its
   right, hence -1
```

```
Input : a[] = [1, 1, 1, 2, 2, 2, 2, 11, 3, 3]
Output : [2, 2, 2, -1, -1, -1, -1, 3, -1, -1]
```

https://practice.geeksforgeeks.org/problems/9656e96f6eaee49e67400fa2aed7833c8d9846b8/0?category%5B%5D=Hash
'''
class Solution:
    def print_next_greater_freq(self,arr,n):
        # code here
        if len(arr) == 1:
            return [-1]

        fre = {}
        for i in arr:
            fre[i] = fre.get(i, 0) + 1

        answer = []
        stack = []
        for i in range(len(arr) - 1, -1, -1):
            next_popped = arr.pop()
            while stack and fre[next_popped] >= fre[stack[-1]]:
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

Given a stack of integers, sort it in ascending order using another temporary stack.

**Examples:**

```
Input : [34, 3, 31, 98, 92, 23]
Output : [3, 23, 31, 34, 92, 98]

Input : [3, 5, 1, 4, 2, 8]
Output : [1, 2, 3, 4, 5, 8]

https://www.geeksforgeeks.org/sort-stack-using-temporary-stack/
```
'''
class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def sorted(self, s: 'list[int]'):
        # Code here
        tempstack = [s.pop()]
        while s:
            while s and tempstack[-1] < s[-1]:
                tempstack.append(s.pop())
            if not s:
                break
            temp = s.pop()
            while tempstack and tempstack[-1] > temp:
                s.append(tempstack.pop())
            tempstack.append(temp)
            continue
        return tempstack

'''
💡 **Question 3**

Given a stack with **push()**, **pop()**, and **empty()** operations, The task is to delete the **middle** element ****of it without using any additional data structure.

Input  : Stack[] = [1, 2, 3, 4, 5]

Output : Stack[] = [1, 2, 4, 5]

Input  : Stack[] = [1, 2, 3, 4, 5, 6]

Output : Stack[] = [1, 2, 4, 5, 6]

https://practice.geeksforgeeks.org/problems/delete-middle-element-of-a-stack/1
'''
from math import ceil

class Solution:

    #Function to delete middle element of a stack.
    def deleteMid(self, s: 'list[int]', sizeOfStack: int):
        # code here
        extra = []
        middle = ceil(sizeOfStack / 2) - (1 if sizeOfStack % 2 != 0 else 0)
        for i in range(middle):
            extra.append(s.pop())
        s.pop()
        while extra:
            s.append(extra.pop())
        return s

'''
💡 **Question 4**

Given a Queue consisting of first **n** natural numbers (in random order). The task is to check whether the given Queue elements can be arranged in increasing order in another Queue using a stack. The operation allowed are:

1. Push and pop elements from the stack
2. Pop (Or Dequeue) from the given Queue.
3. Push (Or Enqueue) in the another Queue.

**Examples :**

Input : Queue[] = { 5, 1, 2, 3, 4 } 

Output : Yes 

Pop the first element of the given Queue 

i.e 5. Push 5 into the stack. 

Now, pop all the elements of the given Queue and push them to second Queue. 

Now, pop element 5 in the stack and push it to the second Queue.   

Input : Queue[] = { 5, 1, 2, 6, 3, 4 } 

Output : No 

Push 5 to stack. 

Pop 1, 2 from given Queue and push it to another Queue. 

Pop 6 from given Queue and push to stack. 

Pop 3, 4 from given Queue and push to second Queue. 

Now, from using any of above operation, we cannot push 5 into the second Queue because it is below the 6 in the stack.

https://www.geeksforgeeks.org/check-queue-can-sorted-another-queue-using-stack/1
'''


'''
💡 **Question 5**

Given a number , write a program to reverse this number using stack.

**Examples:**

```
Input : 365
Output : 563

Input : 6899
Output : 9986
```

https://www.geeksforgeeks.org/reverse-number-using-stack/
'''
def reverse(S):
    #Add code here
    s = []
    S = str(S)
    while S:
        s.append(S[0])
        S = S[1:]
    while s:
        S += s.pop()
    return S

'''
💡 **Question 6**

Given an integer k and a **[queue](https://www.geeksforgeeks.org/queue-data-structure/)** of integers, The task is to reverse the order of the first **k** elements of the queue, leaving the other elements in the same relative order.

Only following standard operations are allowed on queue.

- **enqueue(x) :** Add an item x to rear of queue
- **dequeue() :** Remove an item from front of queue
- **size() :** Returns number of elements in queue.
- **front() :** Finds front item.

https://practice.geeksforgeeks.org/problems/reverse-first-k-elements-of-queue/1
'''
def modifyQueue(q: 'list[int]', k):
    # code here
    j = len(q) - k
    firstk = []
    for i in range(k):
        o = q[0]
        q.remove(q[0])
        firstk.append(o)
    # firstk.reverse()
    while firstk:
        q.append(firstk.pop())
    for i in range(j):
        o = q[0]
        q.remove(q[0])
        q.append(o)
    return q

'''
💡 **Question 7**

Given a sequence of n strings, the task is to check if any two similar words come together and then destroy each other then print the number of words left in the sequence after this pairwise destruction.

**Examples:**

Input : ab aa aa bcd ab

Output : 3

*As aa, aa destroys each other so,*

*ab bcd ab is the new sequence.*

Input :  tom jerry jerry tom

Output : 0

*As first both jerry will destroy each other.*

*Then sequence will be tom, tom they will also destroy*

*each other. So, the final sequence doesn’t contain any*

*word.*

https://practice.geeksforgeeks.org/problems/string-manipulation3706/1?utm_source=gfg
'''
class Solution:
    def removeAdj(self,v,n):
        # Your code goes here
        stack = []
        for elem in v:
            if stack and stack[-1] == elem:
                stack.pop()
                continue
            else:
                stack.append(elem)
        return len(stack)

'''
💡 **Question 8**

Given an array of integers, the task is to find the maximum absolute difference between the nearest left and the right smaller element of every element in the array.

**Note:** If there is no smaller element on right side or left side of any element then we take zero as the smaller element. For example for the leftmost element, the nearest smaller element on the left side is considered as 0. Similarly, for rightmost elements, the smaller element on the right side is considered as 0.

**Examples:**
```
Input : arr[] = {2, 1, 8}
Output : 1
Left smaller  LS[] {0, 0, 1}
Right smaller RS[] {1, 0, 0}
Maximum Diff of abs(LS[i] - RS[i]) = 1

Input  : arr[] = {2, 4, 8, 7, 7, 9, 3}
Output : 4
Left smaller   LS[] = {0, 2, 4, 4, 4, 7, 2}
Right smaller  RS[] = {0, 3, 7, 3, 3, 3, 0}
Maximum Diff of abs(LS[i] - RS[i]) = 7 - 3 = 4

Input : arr[] = {5, 1, 9, 2, 5, 1, 7}
Output : 1
```

https://practice.geeksforgeeks.org/problems/maximum-difference-1587115620/1
'''
class Solution:
    # Your task is to complete this function
    # Function should return an integer denoting the required answer
    def getLeftSmallestElements(self, arr: 'list[int]', n: int):
        if len(arr) == 1:
            return [0]

        answer = []
        stack = []
        arr.reverse()
        for i in range(len(arr) - 1, -1, -1):
            next_popped = arr.pop()
            while stack and stack[-1] >= next_popped:
                stack.pop()
            if not stack:
                answer.append(0)
                stack.append(next_popped)
                continue
            else:
                answer.append(stack[-1])
                stack.append(next_popped)

        return answer

    def getRightSmallestElements(self, arr: 'list[int]', n: int):
        if len(arr) == 1:
            return [0]

        answer = []
        stack = []
        for i in range(len(arr) - 1, -1, -1):
            next_popped = arr.pop()
            while stack and stack[-1] >= next_popped:
                stack.pop()
            if not stack:
                answer.append(0)
                stack.append(next_popped)
                continue
            else:
                answer.append(stack[-1])
                stack.append(next_popped)

        return answer[-1::-1]

    def findMaxDiff(self, arr: 'list[int]', n: int):
        # Code here
        left_smallest_elements = self.getLeftSmallestElements(arr[:], n)
        right_smallest_elements = self.getRightSmallestElements(arr[:], n)
        max_abs_diff = 0
        for i in range(n):
            diff = left_smallest_elements[i] - right_smallest_elements[i]
            max_abs_diff = max(max_abs_diff, abs(diff))
        return max_abs_diff

