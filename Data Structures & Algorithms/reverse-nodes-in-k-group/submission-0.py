# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        group_prev = dummy

        while True:
            # dummy point to kth node (tail)
            kth = group_prev
            for _ in range(k):   
                kth = kth.next
                if not kth:
                    return dummy.next   
            next_head = kth.next

            # cut connection from kth -> next head
            kth.next = None

            # reverse before
            prev = None
            cur = group_prev.next
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            # reconnect tail -> next head
            # group prev -> tail.     nexthead ...
            tail = group_prev.next
            group_prev.next = kth
            tail.next = next_head  
            group_prev = tail

        return dummy.next
        
        