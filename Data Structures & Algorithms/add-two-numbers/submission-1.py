# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        head = dummy
        incre = 0
        while l1 or l2 or incre:
            v1 = l1.val if l1 else 0 
            v2 = l2.val if l2 else 0

            s = (v1 + v2 + incre) % 10
            incre = (v1 + v2 + incre) // 10

            head.next = ListNode(val=s)
            head = head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next



        