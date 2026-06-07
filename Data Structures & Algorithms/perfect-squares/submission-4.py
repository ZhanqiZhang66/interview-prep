class Solution:
    def numSquares(self, n: int) -> int:
        # the least number of perfect numsquares that sum to n
        # =  1
        # + the least number of perfect numsquares that sum to n - x**2
        dp = list(range(0, n+1)) # the min number of ways to adds up to n using first i elements

        for x in range(1, int(n ** 0.5) + 1):
            for a in range(x**2, n+1):
                dp[a] = min(dp[a], 1 + dp[a - x ** 2])
        return dp[-1]

    