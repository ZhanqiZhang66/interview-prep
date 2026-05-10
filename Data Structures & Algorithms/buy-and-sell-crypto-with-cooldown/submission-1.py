class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # t = len(prices)
        # dp = [[0 for _ in range(t+1)] for _ in range(2)]
        # # profit with cool, profit wihtout cooldown

        # for i in range(t-1, -1, -1):
        #     for previous_is_cooldown in [True, False]:
        #         if not previous_is_cooldown:
        #             hold = dp[0][i+1] if i+1 < t else 0
        #             buy = dp[1][i+1] - prices[i] if i + 1 < t else -prices[i]
        #             dp[0][i] = max(hold, buy)
        #         else:
        #             sell = dp[1][i+2] + prices[i] if i+2 < t else prices[i]
        #             hold = dp[0][i+1] if i+1 < t else 0
        #             dp[1][i] = max(sell, hold)
        # return dp[1][0]
        n = len(prices)
        dp0 = [0] * (n+2)
        dp1 = [0] * (n+2)
        dp1[1] = -prices[0]
        for i in range(2, n+2):
            dp0[i] = max(dp0[i-1], dp1[i-1]+prices[i-2])
            dp1[i] = max(dp1[i-1], dp0[i-2]-prices[i-2])
        return dp0[-1]


























        # n = len(prices)
        # dp = [[0] * 2 for _ in range(n+1)]

        # for i in range(n-1, -1, -1):
        #     for buy in [True, False]:
        #         if buy:
        #             #  hold, buy,
        #             hold = dp[i+1][True] if i+1 < n else 0
        #             buy = dp[i+1][False] - prices[i] if i+1 < n else - prices[i]
        #             dp[i][1] = max(hold, buy)

        #         else:
        #             # hold or sell
        #             hold = dp[i+1][False] if i+1 < n else 0
        #             sell = dp[i+2][True] + prices[i] if i+2 < n else prices[i] 
        #             dp[i][0] = max(hold, sell)
        # return dp[0][1]