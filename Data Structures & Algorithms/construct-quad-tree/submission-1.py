"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        if sum(sum(row) for row in grid) == 0:
            return Node(val=0,
                        isLeaf=True,
                        topLeft=None,
                        topRight=None,
                        bottomLeft=None,
                        bottomRight=None
                        )
        elif sum(sum(row) for row in grid) == len(grid) ** 2:
            return Node(val=1,
                        isLeaf=True,
                        topLeft=None,
                        topRight=None,
                        bottomLeft=None,
                        bottomRight=None
                        )
        else:
            node = Node(val=1, isLeaf=False)
            n = len(grid[0])

            if n > 1:
                print([row[0: n//2] for row in grid[0: n//2]])
                node.topLeft = self.construct([row[0: n//2] for row in grid[0: n//2]])
                node.topRight = self.construct([row[n//2: ] for row in grid[0: n//2]])
                node.bottomLeft = self.construct([row[0: n//2] for row in grid[n//2: ]])
                node.bottomRight = self.construct([row[n//2: ] for row in grid[n//2: ]])
        return node

        