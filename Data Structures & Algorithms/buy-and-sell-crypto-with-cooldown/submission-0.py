class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for buy in [True, False]:
                if buy:
                    #  hold, buy,
                    hold = dp[i+1][True] if i+1 < n else 0
                    buy = dp[i+1][False] - prices[i] if i+1 < n else - prices[i]
                    dp[i][1] = max(hold, buy)

                else:
                    # hold or sell
                    hold = dp[i+1][False] if i+1 < n else 0
                    sell = dp[i+2][True] + prices[i] if i+2 < n else prices[i] 
                    dp[i][0] = max(hold, sell)
        return dp[0][1]