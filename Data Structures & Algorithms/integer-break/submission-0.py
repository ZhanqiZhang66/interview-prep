class Solution:
    def integerBreak(self, n: int) -> int:
        # max product of n = max(max product of n (cannot regress), i * max_product of n - i, i * n-i)
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * dp[i - j], j * (i - j))
        return dp[n]

        