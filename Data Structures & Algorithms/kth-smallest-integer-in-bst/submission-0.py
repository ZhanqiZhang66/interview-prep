# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            if not node:
                return []
            curr_smallest = dfs(node.left) + [node.val] + dfs(node.right)
            
            return curr_smallest
                
        sorted_tree = dfs(root)      
        return sorted_tree[k-1]
        