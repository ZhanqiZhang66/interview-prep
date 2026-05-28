# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter = max(diameter(node))
        # diameter(node) = maxdepth(left) + maxdepth(right)
        res = 0
        def maxDepth(node):
            nonlocal res
            if not node:
                return -1
            left = maxDepth(node.left)
            right = maxDepth(node.right)
            res = max(res, left + right + 2)
            return 1 + max(left, right)
        maxDepth(root)
        return res
        