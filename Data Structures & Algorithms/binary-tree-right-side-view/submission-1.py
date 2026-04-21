# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        ans = []
        while queue:
            for i in range(len(queue)):
                pop = queue.popleft()    
                if pop.left:
                    queue.append(pop.left)
                if pop.right:
                    queue.append(pop.right)
            ans.append(pop.val)
        return ans


        