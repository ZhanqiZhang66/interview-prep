# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            # if not root.left and not root.right:
            #     return root.val
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, root.val, left + root.val, right + root.val, left + right + root.val)
            return max(left, right, 0) + root.val
        dfs(root)
        return res
            

        