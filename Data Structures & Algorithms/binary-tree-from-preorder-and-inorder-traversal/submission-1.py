# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # pre order: root, left, right 0
        # in order: left, root, right inorder{preorder[0]} = root index 
        if not preorder or not inorder:
            return None
        inorder_dict = {val: ind for ind, val in enumerate(inorder)}
        root = TreeNode(preorder[0])
        mid = inorder_dict[preorder[0]]
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        

        return root
        


        