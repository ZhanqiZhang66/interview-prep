"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        

        def dfs(node):
            # if node in cloned:
            #     return cloned[node]

            copy = Node(node.val)
            cloned[node] = copy
            for n in node.neighbors:
                if n not in cloned:
                    copy_neighbor = dfs(n)
                    copy.neighbors.append(copy_neighbor)
                else:
                    copy.neighbors.append(cloned[n])
            return copy
                # print(f"search nei's nei from here {cloned}")
                
  
        cloned = {}
       
        
       
        return dfs(node) if node else None       