# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # dp: [rob this, don't rob this]the maximum amount of money the thief can rob
        def dfs(root):
            if not root:
                return [0, 0]
            # two choices: 
            #rob me, + not rob my child 
            left = dfs(root.left)
            right = dfs(root.right)
            rob = root.val + left[1] + right[1]
            #not rob me -> max possible from my children
            notrob = max(left) + max(right)
            return [rob, notrob]
        return max(dfs(root))

        