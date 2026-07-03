# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        inorder_dict = {val: i for i, val in enumerate(inorder)}
        
        root_idx = inorder_dict[preorder[0]]
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:1 + root_idx], inorder[: root_idx])
        root.right = self.buildTree(preorder[1 + root_idx:], inorder[root_idx + 1:])
        return root
        