"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old2copy = collections.defaultdict(lambda: Node(0))
        old2copy[None] = None
        cur = head
        while cur:
            old2copy[cur].val = cur.val
            old2copy[cur].next = old2copy[cur.next]
            old2copy[cur].random = old2copy[cur.random]
            cur = cur.next
        return old2copy[head]