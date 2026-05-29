# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def left_tree_rightmost(root):
            while root and root.right:
                root = root.right
            return root
         
        if not root:
            return root
        if root.val == key:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                to_replace = left_tree_rightmost(root.left)
                root.val = to_replace.val
                root.left = self.deleteNode(root.left, to_replace.val)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
        

        