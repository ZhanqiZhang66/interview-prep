class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # (. -> ( -> ( or )
        res = []
        def backtrack(curr, n_left, n_right):
            if n_left == n_right == n:
                res.append("".join(curr.copy()))
                return

            if n_left < n:
                curr.append("(")
                backtrack(curr, n_left+1, n_right)
                curr.pop()
            if n_right < n_left:
                curr.append(")")
                backtrack(curr, n_left, n_right+1)
                curr.pop()
        backtrack([], 0, 0)
        return res

            
