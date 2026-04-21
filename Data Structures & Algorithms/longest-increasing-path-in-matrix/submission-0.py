class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        DIRs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        path = [(matrix[i][j], i, j) for i in range(R) for j in range(C)]
        path.sort()

        dp = [[1] * C for _ in range(R)]

        for v, i, j in path:
            for dr, dc in DIRs:
                r = i + dr
                c = j + dc
                if r in range(R) and c in range(C) and v < matrix[r][c]:
                    dp[r][c] = max(dp[r][c], 1 + dp[i][j]) 
        return max(max(row for row in dp))

        # R, C = len(matrix), len(matrix[0])
        # DIRs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # def dfs(r, c, prev):
        #     if r not in range(R) or c not in range(C) or matrix[r][c] >= prev:
        #         return 0
        #     res = 1
        #     for dr, dc in DIRs:
        #         rr = r + dr
        #         cc = c + dc
        #         res = max(res, 1 + dfs(rr, cc, matrix[r][c]))
        #     return res

        # length = 0
        # for r in range(R):
        #     for c in range(C):
        #         length = max(length, dfs(r, c, float('inf')))
        # return length
