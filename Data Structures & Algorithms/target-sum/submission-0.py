class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(n-1, -1, -1):
            nxt = defaultdict(int)
            for a, count in dp.items():
                nxt[a - nums[i]] += count
                nxt[a + nums[i]] += count
            dp = nxt
        return dp[target]
        