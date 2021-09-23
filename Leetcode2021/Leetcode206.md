# Leetcode206

The classic reverse a linked list. This done in iteration is a wee bit more efficient for python. I think this implementation is a wee bit verbose, there should be a better way to implement without explicitely setting the base to be None, but on the fly this is what I came up with.

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        point = head
        toAdd = point.next
        head.next = None

        while toAdd is not None:
            tmp = toAdd.next
            toAdd.next = point
            point = toAdd
            toAdd = tmp
        return point
            
```