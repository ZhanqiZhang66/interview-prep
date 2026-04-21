# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSametree(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            return isSametree(root.left, subRoot.left) and isSametree(root.right, subRoot.right)

        if not subRoot:
            return True
        if not root:
            return False
        if isSametree(root, subRoot):
            return True
        #     return isSametree(root, subRoot)
        print(f"not same val {isSametree(root.left, subRoot)} or {isSametree(root.right, subRoot)}")
        return isSametree(root.left, subRoot) or isSametree(root.right, subRoot)

        # if not root and not subRoot:
        #     return True
        # if not root or not subRoot:
        #     return False
        # if root.val == subRoot.val:
        #     left = self.isSubtree(root.left, subRoot.left)
        #     right = self.isSubtree(root.left, subRoot.right)
        #     return left and right
        # else:
        #     left = self.isSubtree(root.left, subRoot)
        #     right = self.isSubtree(root.right, subRoot)
        #     return left or right