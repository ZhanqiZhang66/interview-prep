# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(root):
            nonlocal res
            if not root:
                res.append("null")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        res = data.split(",")
        
        def dfs(i):
            nonlocal res
           
            if res[i] == "null":
                return None, i+1
            root = TreeNode(res[i])
            i += 1
            root.left, i = dfs(i)
            root.right, i = dfs(i)
            return root, i
        root, _ = dfs(0)
        return root
