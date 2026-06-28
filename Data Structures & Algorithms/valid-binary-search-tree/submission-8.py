# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, minn, maxx):
            if not root:
                return True
            # print(root.val)
            if root.val >= maxx or root.val <= minn:
                return False
            left = dfs(root.left, minn, min(root.val, maxx))
            print(minn)
            print(min(root.val, maxx))
            print(left)
            right = dfs(root.right, max(root.val, minn), maxx)
         
            
            print(right)
            return left and right
        return dfs(root, float('-inf'), float('inf'))
        

        
        