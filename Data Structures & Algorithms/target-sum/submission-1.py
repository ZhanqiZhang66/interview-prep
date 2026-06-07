class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # for each number, to know if this can get to target
        #     -----i-----
        # we need to know at previous step, how many ways tgt - num can be formed + how many ways tg + nums can be formed
        #                    ------i------               -----a-----                              ----a----

        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for a, count in dp[i - 1].items():
                print(a)
                dp[i][a + nums[i-1]] += count
                dp[i][a - nums[i-1]] += count
        return dp[n][target]

        
        