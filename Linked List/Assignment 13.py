class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

'''
💡 **Question 1**

Given two linked list of the same size, the task is to create a new linked list using those linked lists. The condition is that the greater node among both linked list will be added to the new linked list.

**Examples:**
```
Input: list1 = 5->2->3->8
list2 = 1->7->4->5
Output: New list = 5->7->4->8

Input:list1 = 2->8->9->3
list2 = 5->3->6->4
Output: New list = 5->8->9->4
```

https://www.geeksforgeeks.org/create-new-linked-list-from-two-given-linked-list-with-greater-element-at-each-node/
'''
class Solution:
    def createNew(self, head1, head2):
        head3 = head1 if head1.val > head2.val else head2.val
        head1, head2 = head1.next, head2.next
        while head1:
            head3.next = head1 if head1.val > head2.val else head2.val
            head1, head2 = head1.next, head2.next
        return head3

'''
💡 **Question 2**

Write a function that takes a list sorted in non-decreasing order and deletes any duplicate nodes from the list. The list should only be traversed once.

For example if the linked list is 11->11->11->21->43->43->60 then removeDuplicates() should convert the list to 11->21->43->60.

**Example 1:**

```
Input:
LinkedList: 
11->11->11->21->43->43->60
Output:
11->21->43->60
```

**Example 2:**
```
Input:
LinkedList: 
10->12->12->25->25->25->34
Output:
10->12->25->34
```

https://practice.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1
'''
#Function to remove duplicates from sorted linked list.
def removeDuplicates(head):
    #code here
    _head = head
    while _head and _head.next:
        while _head.data == _head.next.data:
            _head.next = _head.next.next
        _head = _head.next
    return head

'''
💡 **Question 3**

Given a linked list of size **N**. The task is to reverse every **k** nodes (where k is an input to the function) in the linked list. If the number of nodes is not a multiple of *k* then left-out nodes, in the end, should be considered as a group and must be reversed (See Example 2 for clarification).

**Example 1:**

```
Input:
LinkedList: 1->2->2->4->5->6->7->8
K = 4
Output:4 2 2 1 8 7 6 5
Explanation:
The first 4 elements 1,2,2,4 are reversed first
and then the next 4 elements 5,6,7,8. Hence, the
resultant linked list is 4->2->2->1->8->7->6->5.

```

**Example 2:**
```
Input:
LinkedList: 1->2->3->4->5
K = 3
Output:3 2 1 5 4
Explanation:
The first 3 elements are 1,2,3 are reversed
first and then elements 4,5 are reversed.Hence,
the resultant linked list is 3->2->1->5->4.
```

https://practice.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1
'''
class Solution:
    def reverse(self,head, k):
        # Code here
        new_head, prev_tail, tail = None, None, None
        while head:
            i = 0
            prev_tail = tail
            tail = head
            
            prev = None
            curr = head
            while i < k and curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                i += 1

            if not new_head:
                new_head = prev
            head = curr or prev
            if prev_tail:
                prev_tail.next = prev
            if not temp:
                break
        return new_head

'''
💡 **Question 4**

Given a linked list, write a function to reverse every alternate k nodes (where k is an input to the function) in an efficient way. Give the complexity of your algorithm.

**Example:**
```
Inputs:   1->2->3->4->5->6->7->8->9->NULL and k = 3
Output:   3->2->1->4->5->6->9->8->7->NULL.
```

https://www.geeksforgeeks.org/reverse-alternate-k-nodes-in-a-singly-linked-list/
'''
class Solution:
    def reverseAlternate(self, head: ListNode, k):
        curr = head
        prev_tail = None
        new_head = None

        while head:
            i = 0
            first_head = curr

            prev = None
            while i < k and curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                i += 1

            if prev_tail:
                prev_tail.next = prev
            if not new_head:
                new_head = prev
            if not temp or not curr:
                break

            first_head.next = temp
            i = 0
            while i < k:
                prev_tail = curr
                curr = curr.next
                if not curr:
                    break
                i += 1
        return new_head

'''
💡 **Question 5**

Given a linked list and a key to be deleted. Delete last occurrence of key from linked. The list may have duplicates.

**Examples**:
```
Input:   1->2->3->5->2->10, key = 2
Output:  1->2->3->5->10
```

https://www.geeksforgeeks.org/delete-last-occurrence-of-an-item-from-linked-list/
'''
class Solution:
    def removeLastOccurrence(self, head: ListNode, k: int):
        curr = head
        prev = curr

        while curr and curr.next:
            if curr.next.val == k:
                prev = curr
            curr = curr.next

        prev.next = prev.next.next
        return head

'''
💡 **Question 6**

Given two sorted linked lists consisting of **N** and **M** nodes respectively. The task is to merge both of the lists (in place) and return the head of the merged list.

**Examples:**

Input: a: 5->10->15, b: 2->3->20

Output: 2->3->5->10->15->20

Input: a: 1->1, b: 2->4

Output: 1->1->2->4

https://www.geeksforgeeks.org/merge-two-sorted-linked-lists/
https://leetcode.com/problems/merge-two-sorted-lists/description/
'''
class Solution:
    def mergeTwoLists(
        self, 
        list1: Optional[ListNode], 
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1

        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

'''
💡 **Question 7**

Given a **Doubly Linked List**, the task is to reverse the given Doubly Linked List.

**Example:**
```
Original Linked list 10 8 4 2
Reversed Linked list 2 4 8 10
```

https://practice.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1
'''
class Solution:
    def reverseDLL(self, head):
        #return head after reversing
        if not head.next:
            return head
        while head:
            head.next, head.prev = head.prev, head.next
            head = head.prev
            if not head.next:
                head.next = head.prev
                head.prev = None
                break
        return head

'''
💡 **Question 8**

Given a doubly linked list and a position. The task is to delete a node from given position in a doubly linked list.

**Example 1:**

```
Input:
LinkedList = 1 <--> 3 <--> 4
x = 3
Output:1 3
Explanation:After deleting the node at
position 3 (position starts from 1),
the linked list will be now as 1->3.

```

**Example 2:**
```
Input:
LinkedList = 1 <--> 5 <--> 2 <--> 9
x = 1
Output:5 2 9
```

https://practice.geeksforgeeks.org/problems/delete-node-in-doubly-linked-list/1
'''
class Solution:
    def deleteNode(self, head, x):
        # Code here
        curr = head
        for i in range(1,x):
            curr = curr.next
        if curr.prev:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        return head
