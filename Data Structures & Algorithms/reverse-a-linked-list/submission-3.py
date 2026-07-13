# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev
# notes: I kepte writing prev = ListNode which is wrong. because last node is None, and None is not ListNode(val=0)
# notes 2: the while condition is the condition to process till the last node, 
# i wrote head.next, which was wrong and it will skip the last node. only slow fast pointer has fast and fast.next

# note 3: I wrote return prev.next becuase this appears in other code. I need to think carefully what to return, 
# instead of relying on vague memory 