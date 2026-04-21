class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R, C = len(matrix), len(matrix[0])
        res = []

        def dfs(height, width, r, c, dr, dc):
            if height == 0 or width == 0:
                return
            for i in range(width):
                r += dr
                c += dc
                res.append(matrix[r][c])
            dfs(width, height - 1, r, c, dc, -dr)

        dfs(R, C, 0, -1, 0, 1)
        return res

        