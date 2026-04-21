# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_val = root.val
        def dfs(node):
            nonlocal max_val
            if not node:
                return 0 
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)

            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)

            max_val = max(leftMax + rightMax + node.val, max_val)

            return node.val + max(leftMax, rightMax)
        dfs(root)
        return max_val




        # max_val = float('-inf')
        # def dfs(node, sum_upward):
        #     nonlocal max_val
        #     if not node:
        #         return 0
        #     prev_um_upward = sum_upward
        #     sum_upward += node.val 
        #     left_sum = dfs(node.left, sum_upward) + node.val
        #     right_sum = dfs(node.right, sum_upward) + node.val
        #     path_sum = left_sum + right_sum - node.val
        #     max_val = max(
        #                 max_val, \
        #                 left_sum  + prev_um_upward, \
        #                 right_sum + prev_um_upward, \
        #                 path_sum, \
        #                 left_sum, \
        #                 right_sum)
            
        #     return max(0, left_sum, right_sum)
        # dfs(root, 0)
        # return max_val
        