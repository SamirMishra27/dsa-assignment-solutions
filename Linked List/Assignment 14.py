class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional, List

'''
💡 **Question 1**

Given a linked list of **N** nodes such that it may contain a loop.

A loop here means that the last node of the link list is connected to the node at position X(1-based index). If the link list does not have any loop, X=0.

Remove the loop from the linked list, if it is present, i.e. unlink the last node which is forming the loop.
Example 1:
```
Input:
N = 3
value[] = {1,3,4}
X = 2
Output:1
Explanation:The link list looks like
1 -> 3 -> 4
     ^    |
     |____|
A loop is present. If you remove it
successfully, the answer will be 1.

```

Example 2:
```
Input:
N = 4
value[] = {1,8,3,4}
X = 0
Output:1
Explanation:The Linked list does not
contains any loop.
```


https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1
'''
class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        face, tail = head, head
        while tail.next and tail.next.next:
            face = face.next
            tail = tail.next.next
            if face == tail:
                break
        if not tail or not tail.next:
            return
        prev = head
        while head != face:
            head = head.next
            face = face.next
        prev.next = None

'''
💡 **Question 2**

A number **N** is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.

**Example 1:**

```
Input:
LinkedList: 4->5->6
Output:457

```

**Example 2:**
```
Input:
LinkedList: 1->2->3
Output:124
```

https://practice.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1
'''
class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    def addOne(self, head):
        #Returns new head of linked List.
        if head.next:
            head = self.reverse(head)
        head.data += 1
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
            if prev.data == 10:
                prev.data = 0
                if head:
                    head.data += 1
                else:
                    node = ListNode(1)
                    node.next = prev
                    prev = node
        return prev

'''
<aside>
💡 **Question 3**

Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:(i) a **next** pointer to the next node,(ii) a **bottom** pointer to a linked list where this node is head.Each of the sub-linked-list is in sorted order.Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. **Note:** The flattened list will be printed using the bottom pointer instead of next pointer.

**Example 1:**

```
Input:
5 -> 10 -> 19 -> 28
|     |     |     |
7     20    22   35
|           |     |
8          50    40
|                 |
30               45
Output: 5-> 7-> 8- > 10 -> 19-> 20->
22-> 28-> 30-> 35-> 40-> 45-> 50.
Explanation:
The resultant linked lists has every
node in a single level.(Note:| represents the bottom pointer.)

```

**Example 2:**
```
Input:
5 -> 10 -> 19 -> 28
|          |
7          22
|          |
8          50
|
30
Output: 5->7->8->10->19->22->28->30->50
Explanation:
The resultant linked lists has every
node in a single level.

(Note:| represents the bottom pointer.)
```

https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1
'''


'''
💡 **Question 4**

You are given a special linked list with **N** nodes where each node has a next pointer pointing to its next node. You are also given **M** random pointers, where you will be given **M** number of pairs denoting two nodes **a** and **b**  **i.e. a->arb = b** (arb is pointer to random node)**.**

... Question is too big.

https://practice.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1
'''

'''
💡 **Question 5**

Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return *the reordered list*.

The **first** node is considered **odd**, and the **second** node is **even**, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in `O(1)` extra space complexity and `O(n)` time complexity.

**Example 1:**

!https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg

```
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

```

**Example 2:**
```
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
```

https://leetcode.com/problems/odd-even-linked-list/
'''
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        o = 0
        prev, curr, odd_last, first_even = None, head, None, head.next
        while curr.next:
            curr._next = curr.next.next if curr.next.next else None
            prev = curr
            curr = curr.next
            o += 1
        curr._next = None
        odd_last = curr if o % 2 == 0 else prev
        odd_last._next = first_even
        curr = head
        while curr:
            temp = curr.next
            curr.next = curr._next
            del curr._next
            curr = temp
        return head

'''
💡 **Question 6**

Given a singly linked list of size **N**. The task is to **left-shift** the linked list by **k** nodes, where **k** is a given positive integer smaller than or equal to length of the linked list.

**Example 1:**

```
Input:
N = 5
value[] = {2, 4, 7, 8, 9}
k = 3
Output:8 9 2 4 7
Explanation:Rotate 1:4 -> 7 -> 8 -> 9 -> 2
Rotate 2: 7 -> 8 -> 9 -> 2 -> 4
Rotate 3: 8 -> 9 -> 2 -> 4 -> 7

```

**Example 2:**
```
Input:
N = 8
value[] = {1, 2, 3, 4, 5, 6, 7, 8}
k = 4
Output:5 6 7 8 1 2 3 4
```

https://practice.geeksforgeeks.org/problems/rotate-a-linked-list/1
'''
class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        p, c, i = None, head, 0
        while i < k:
            p = c
            c = c.next
            i += 1
        if not c:
            return head
        p.next = None
        p = c
        while c.next:
            c = c.next
        c.next = head
        return p

'''
💡 **Question 7**

You are given the `head` of a linked list with `n` nodes.

For each node in the list, find the value of the **next greater node**. That is, for each node, find the value of the first node that is next to it and has a **strictly larger** value than it.

Return an integer array `answer` where `answer[i]` is the value of the next greater node of the `ith` node (**1-indexed**). If the `ith` node does not have a next greater node, set `answer[i] = 0`.

**Example 1:**

!https://assets.leetcode.com/uploads/2021/08/05/linkedlistnext1.jpg

```
Input: head = [2,1,5]
Output: [5,5,0]

```

**Example 2:**
```
Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]
```

https://leetcode.com/problems/next-greater-node-in-linked-list/
'''
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        a = []
        c1, c2 = head, head
        while c2:
            if c1.val < c2.val:
                while c1 != c2:
                    a.append(c2.val)
                    c1 = c1.next
                c1 = c2
                continue
            if not c2.next and c1 != c2:
                a.append(0)
                c1, c2 = c1.next, c1.next
                continue
            c2 = c2.next
        a.append(0)
        return a

'''
💡 **Question 8**

Given the `head` of a linked list, we repeatedly delete consecutive sequences of nodes that sum to `0` until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

(Note that in the examples below, all sequences are serializations of `ListNode` objects.)

**Example 1:**

```
Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.

```

**Example 2:**

```
Input: head = [1,2,3,-3,4]
Output: [1,2,4]

```

**Example 3:**
```
Input: head = [1,2,3,-3,-2]
Output: [1]
```


'''

