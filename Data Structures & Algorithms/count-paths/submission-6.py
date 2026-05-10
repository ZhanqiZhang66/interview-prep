class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * n
        curr = [1] * n
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                curr[j] = prev[j] + curr[j+1]
            tmp = prev
            prev = curr
            curr = prev
        return prev[0]
                



























        # dp = [[0] * (n+1) for _ in range(m+1)]

        # dp[m-1][n-1] = 1

        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #             dp[i][j] += dp[i+1][j] + dp[i][j+1] 
        # return dp[0][0]
                    
        