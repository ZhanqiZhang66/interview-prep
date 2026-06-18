# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return [0, 0]
            left = dfs(root.left)
            right = dfs(root.right)

            robme = root.val + right[1] + left[1] 
            norobme = max(right) + max(left)
            return [robme, norobme]
        return max(dfs(root))

      

        