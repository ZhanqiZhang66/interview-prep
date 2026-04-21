class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        new_nums = [1] + nums + [1]

        dp = [[0] * (n+2) for _ in range(n+2)]
        #  0 |1               n|    n+1   
        #    (<-  l          ->)
        #         (<-     r  ->)

        for l in range(n, 0, -1):
            for r in range(l, n+1):
                for b in range(l, r+1):
                    # when pop b, [l, b-1]  [b+1, r] are gone except for b
                    # o o  x x x x b x x x x x  o o o
                    # o o [l     ] b [       r] o o o
                    coins = new_nums[l-1] * new_nums[b] * new_nums[r+1]
                    coins += dp[l][b-1] + dp[b+1][r]

                    dp[l][r] = max(dp[l][r], coins)
        return dp[1][n]



        