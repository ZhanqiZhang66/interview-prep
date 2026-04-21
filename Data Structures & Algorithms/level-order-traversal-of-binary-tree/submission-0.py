# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        ans = []

        while queue:
            ans_l = []
            for _ in range(len(queue)):
                pop = queue.popleft()
                ans_l.append(pop.val)

                if pop.left:
                    queue.append(pop.left)
                if pop.right:
                    queue.append(pop.right)
            ans.append(ans_l)
        return ans


        