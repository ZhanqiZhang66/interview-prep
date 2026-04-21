class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        
        if amount == 0:
            return 0
        coins.sort()
        dp = {n: amount}
        m = 0
  
        for i in range(n-1, -1, -1):
            if dp[i+1] % coins[i] == 0:
                m += dp[i+1] // coins[i]
                return m
            if dp[i+1] % coins[i] > 0:
                dp[i] = dp[i+1] % coins[i]
                m += dp[i+1] // coins[i]
            else:
                dp[i] = dp[i+1]
        return -1 if dp[0] > 0 else m
                         
        