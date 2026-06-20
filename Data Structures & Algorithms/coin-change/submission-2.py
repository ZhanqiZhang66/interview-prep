class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # fewest number of coins that you need to make up the exact target amount
        dp = [float('inf')] * (amount + 1) # fewest number of coins that you need to make up the exact amount a 

        # initialization 0 coins need to make 0
        dp[0] = 0

        for coin in coins:
            for a in range(coin, amount + 1):
                # dp[a] could be made
                # 1 we use coin
                # 2 we do not use this coin
                dp[a] = min(dp[a],  dp[a - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
        