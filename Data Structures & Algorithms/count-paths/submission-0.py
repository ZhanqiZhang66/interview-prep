class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        dp[m-1][n-1] = 1
        # dp[m-2][n-1] = 1
        # dp[m-1][n-2] = 1

        DIRS = [[0, 1], [1, 0]]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if 0 <= i+1 < m:
                    dp[i][j] += dp[i+1][j] 
                if 0<= j + 1 < n:
                    dp[i][j] += dp[i][j+1] 
                print(f"update dp[{i}][{j}] = {dp[i][j]}")
        return dp[0][0]
                    
        