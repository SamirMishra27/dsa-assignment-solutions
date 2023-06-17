class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

'''
💡 **Question 1**

Given a singly linked list, delete **middle** of the linked list. For example, if given linked list is 1->2->**3**->4->5 then linked list should be modified to 1->2->4->5.If there are **even** nodes, then there would be **two middle** nodes, we need to delete the second middle element. For example, if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.If the input linked list is NULL or has 1 node, then it should return NULL

**Example 1:**

```
Input:
LinkedList: 1->2->3->4->5
Output:1 2 4 5

```

**Example 2:**
```
Input:
LinkedList: 2->4->6->7->5->1
Output:2 4 6 5 1
```


'''
class Solution:
    def deleteMid(self, head):
        '''
        head:  head of given linkedList
        return: head of resultant llist
        '''
        if not head or not head.next:
            return None
        p, x, y = head, head, head
        while y.next and y.next.next:
            p = x
            x = x.next
            y = y.next.next
            if not y.next or not y.next.next:
                break
        
        if not y.next:
            p.next = x.next
        elif not y.next.next:
            x.next = x.next.next
        return head

'''
💡 **Question 2**

Given a linked list of **N** nodes. The task is to check if the linked list has a loop. Linked list can contain self loop.

**Example 1:**

```
Input:
N = 3
value[] = {1,3,4}
x(position at which tail is connected) = 2
Output:True
Explanation:In above test case N = 3.
The linked list with nodes N = 3 is
given. Then value of x=2 is given which
means last node is connected with xth
node of linked list. Therefore, there
exists a loop.
```

**Example 2:**
```
Input:
N = 4
value[] = {1,8,3,4}
x = 0
Output:False
Explanation:For N = 4 ,x = 0 means
then lastNode->next = NULL, then
the Linked list does not contains
any loop.
```

https://practice.geeksforgeeks.org/problems/detect-loop-in-linked-list/1
'''
class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        tail = head
        while tail.next and tail.next.next:
            head = head.next
            tail = tail.next.next
            if head == tail:
                return True
        return False

'''
💡 **Question 3**

Given a linked list consisting of **L** nodes and given a number **N**. The task is to find the **N**th node from the end of the linked list.

**Example 1:**

```
Input:
N = 2
LinkedList: 1->2->3->4->5->6->7->8->9
Output:8
Explanation:In the first example, there
are 9 nodes in linked list and we need
to find 2nd node from end. 2nd node
from end is 8.

```

**Example 2:**
```
Input:
N = 5
LinkedList: 10->5->100->5
Output:-1
Explanation:In the second example, there
are 4 nodes in the linked list and we
need to find 5th from the end. Since 'n'
is more than the number of nodes in the
linked list, the output is -1.
```

https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1
'''
class Solution:
    #Function to find the data of nth node from the end of a linked list
    def getNthFromLast(head,n):
        #code here
        c, p = head, None
        while c:
            t = c.next
            c.next = p
            p = c
            c = t
        for i in range(1, n):
            p = p.next
            if not p:
                break
        return p.data if p else -1

'''
💡 **Question 4**

Given a singly linked list of characters, write a function that returns true if the given list is a palindrome, else false.

!https://media.geeksforgeeks.org/wp-content/uploads/20220816144425/LLdrawio.png

**Examples:**

> Input: R->A->D->A->R->NULL
> 
> 
> **Output:** Yes
> 
> **Input:** C->O->D->E->NULL
> 
> **Output:** No
> 
https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1
'''
class Solution:
    def findMiddleNode(self, head: ListNode) -> ListNode:
        x, y = head, head.next
        while head.next:
            y = y.next
            if not y:
                return x.next
            y = y.next
            x = x.next
            if not y:
                return x

    def reverseSecondHalf(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mn = self.findMiddleNode(head)
        ln = self.reverseSecondHalf(mn)
        while ln:
            if not head.val == ln.val:
                return False
            head = head.next
            ln = ln.next
        return True

'''
💡 **Question 5**

Given a linked list of **N** nodes such that it may contain a loop.

A loop here means that the last node of the link list is connected to the node at position X(1-based index). If the link list does not have any loop, X=0.

Remove the loop from the linked list, if it is present, i.e. unlink the last node which is forming the loop.

Example 3:
```
Input:
N = 4
value[] = {1,2,3,4}
X = 1
Output:1
Explanation:The link list looks like
1 -> 2 -> 3 -> 4
^              |
|______________|
A loop is present.
If you remove it successfully,
the answer will be 1.
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
💡 **Question 6**

Given a linked list and two integers M and N. Traverse the linked list such that you retain M nodes then delete next N nodes, continue the same till end of the linked list.

Difficulty Level: Rookie

**Examples**:
```
Input:
M = 2, N = 2
Linked List: 1->2->3->4->5->6->7->8
Output:
Linked List: 1->2->5->6

Input:
M = 3, N = 2
Linked List: 1->2->3->4->5->6->7->8->9->10
Output:
Linked List: 1->2->3->6->7->8

Input:
M = 1, N = 1
Linked List: 1->2->3->4->5->6->7->8->9->10
Output:
Linked List: 1->3->5->7->9
```

https://practice.geeksforgeeks.org/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/1
'''
class Solution:
    def skipMdeleteN(self, head, M, N):
        # Code here
        while head:
            for i in range(M):
                head = head.next
                if not head.next:
                    return
            node = head
            for i in range(N):
                head = head.next
            node.next = head

'''
💡 **Question 7**

Given two linked lists, insert nodes of second list into first list at alternate positions of first list.
For example, if first list is 5->7->17->13->11 and second is 12->10->2->4->6, the first list should become 5->12->7->10->17->2->13->4->11->6 and second list should become empty. The nodes of second list should only be inserted when there are positions available. For example, if the first list is 1->2->3 and second list is 4->5->6->7->8, then first list should become 1->4->2->5->3->6 and second list to 7->8.

Use of extra space is not allowed (Not allowed to create additional nodes), i.e., insertion must be done in-place. Expected time complexity is O(n) where n is number of nodes in first list.

https://practice.geeksforgeeks.org/problems/merge-list-alternatingly/1
'''
class Solution:
    def mergeList(head1, head2):
    # Code here
        while head1.next:
            temp1 = head1.next
            temp2 = head2.next
            head1.next = head2
            head2.next = temp1
            head1 = temp1
            head2 = temp2
        return [head1, head2]

'''
💡 **Question 8**

Given a singly linked list, find if the linked list is [circular](https://www.geeksforgeeks.org/circular-linked-list/amp/) or not.

> A linked list is called circular if it is not NULL-terminated and all nodes are connected in the form of a cycle. Below is an example of a circular linked list.
> 

https://practice.geeksforgeeks.org/problems/circular-linked-list/1
'''
def isCircular(head):
    # Code here
    c = head
    while c:
        c = c.next
        if c == head:
            return True
    return False
