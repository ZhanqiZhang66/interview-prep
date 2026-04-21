# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def max_depth(root):
            nonlocal max_diameter
            if not root:
                return 0
            left_h = max_depth(root.left)
            right_h = max_depth(root.right)
            max_diameter = max(max_diameter, left_h + right_h)
            return 1 + max(left_h, right_h)
        max_depth(root)
        return max_diameter
        