# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(l1, l2):
            dummy = ListNode()
            l = dummy
            while l1 and l2:
                if l1.val > l2.val:
                    l.next = l2
                    l2 = l2.next
                else:
                    l.next = l1
                    l1 = l1.next
                l = l.next
            if l1:
                l.next = l1
            else:
                l.next = l2
            return dummy.next

        if not lists:
            return None

        for i in range(1, len(lists)):
            lists[i] = merge2Lists(lists[i - 1], lists[i])
        return lists[-1]

        