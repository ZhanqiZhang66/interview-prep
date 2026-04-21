# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find left middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. reverse h2
        curr = slow.next
        prev = slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3. merge
        h1 = head
        h2 = prev
        while h2:
            h1_next = h1.next
            h2_next = h2.next
            h1.next = h2
            h2.next = h1_next
            h1 = h1_next
            h2 = h2_next
           
        
 


        
        