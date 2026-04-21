# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, NodeWrapper(l))

        dummy = ListNode()
        head = dummy
        while heap:
            smallest = heapq.heappop(heap)
            node = smallest.node
            head.next = node
            head = head.next

            if smallest.node.next:
                heapq.heappush(heap, NodeWrapper(smallest.node.next))
        return dummy.next
    
        