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
        def dfs(grid):
            n = len(grid)

            total = sum(sum(row) for row in grid)
            if total == 0:
                return Node(val=0, 
                            isLeaf=True,
                            topLeft=None,
                            topRight=None,
                            bottomLeft=None,
                            bottomRight=None)
            if total == n * n :
                # print(f"build node {val}")
                return Node(val=1, 
                            isLeaf=True,
                            topLeft=None,
                            topRight=None,
                            bottomLeft=None,
                            bottomRight=None)
            h = len(grid) // 2
            topLeft = [row[:h] for row in grid[:h]]
            topRight = [row[h:] for row in grid[:h]]
            bottomLeft = [row[:h] for row in grid[h:]]
            bottomRight = [row[h:] for row in grid[h:]]
            
            val = grid[0][0]
            
            return Node(
                True,
                False,
                dfs(topLeft),
                dfs(topRight),
                dfs(bottomLeft),
                dfs(bottomRight)
            )
        
        return dfs(grid)
        
        