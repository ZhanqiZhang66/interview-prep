# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_val = float('-inf')
        def dfs(node, sum_upward):
            nonlocal max_val
            if not node:
                return 0
               
            left_sum = dfs(node.left, sum_upward) + node.val
            right_sum = dfs(node.right, sum_upward) + node.val
            path_sum = left_sum + right_sum - node.val
            max_val = max(0, \
                        max_val, \
                        left_sum  + sum_upward, \
                        right_sum + sum_upward, \
                        path_sum, \
                        left_sum, \
                        right_sum)
            sum_upward += node.val 
            return max(0, left_sum, right_sum, path_sum)
        dfs(root, root.val)
        return max_val
        