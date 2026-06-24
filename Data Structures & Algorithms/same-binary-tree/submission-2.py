# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and p or not p and q:
            return False
        if not p and not q:
            return True
        if not p.left and not p.right and not q.left and not q.right:
            return p.val == q.val
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        