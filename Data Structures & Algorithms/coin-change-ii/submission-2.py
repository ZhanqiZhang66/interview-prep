class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for n in coins:
            for a in range(n, amount + 1):
                dp[a] = dp[a] + dp[a - n]
        return dp[-1]
        