# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def max_depth(root):
            nonlocal ans
            if not root:
                return 0
            left_h = max_depth(root.left)
            right_h = max_depth(root.right)
            if abs(left_h - right_h) > 1:
                ans = False
            return 1 + max(left_h, right_h)
        max_depth(root)
        return ans

