class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        # distinct ways to make last m onward of t and last n onward of s match
        dp = [[0] * (m+1) for _ in range(n+1)]
        dp[n][m] = 1
        for i in range(n):
            dp[i][m] = 1

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                # if I don;t use s[i], how many ways to match t[j:]
                dp[i][j] = dp[i+1][j]
                # if I can use s[i], i add 
                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]
   
        return dp[0][0]

        