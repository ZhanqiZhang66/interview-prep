class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [0] * (amount+1)
        dp[0] = 1

        for i in range(n-1, -1, -1):
            for a in range(1, amount+1):
                if a >= coins[i]:
                    dp[a] = dp[a] + dp[a - coins[i]]
        return dp[amount]

        # # maximum ways first i coin can make amount a
        # dp = [[0] * (amount+1) for _ in range(n + 1)]# how many ways i can make up i amount
        
        # # just 1 way to make amount 0 
        # for i in range(n+1):
        #     dp[i][0] = 1
        
        # for i in range(n-1, -1, -1):
        #     for w in range(amount + 1):
        #         # count skip ways
        #         dp[i][w] = dp[i+1][w]
        #         if w >= coins[i]:
        #             # add choose ways when can choose  
        #             dp[i][w] += dp[i][w - coins[i]]

        # return dp[0][amount]