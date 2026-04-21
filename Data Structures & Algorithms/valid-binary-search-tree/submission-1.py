# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_val, max_val):
            if not node:
                return True
            if node.right and (node.right.val <= node.val or node.right.val > max_val):
                return False
            if node.left and (node.left.val >= node.val or node.left.val < min_val):
                return False
            min_val = max(min_val, node.val)
            max_val = min(max_val, node.val)
            return dfs(node.left, -1 *float('inf'), max_val) and dfs(node.right, min_val, float('inf'))

        return dfs(root, -1 *float('inf'), float('inf'))





        # if not root:
        #     return True
        # if (root.left and root.left.val >= root.val) or (root.right and root.right.val <= root.val):
        #     return False
        # else:
        #     return self.isValidBST(root.left) and self.isValidBST(root.right)
        