class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        l = r = 0
        while r < n - 1:
            furthest = 0
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])
            l = r + 1
            r = furthest
            res += 1
        return res
        # n = len(nums)
        # INF = float('inf')
        # dp = [INF] * n
        # dp[n-1] = 0

        # for i in range(n - 2, -1, -1):
        #     jump = nums[i]
        #     max_jump = min(n - 1, i + jump)
        #     for j in range(i + 1, max_jump + 1):
        #         dp[i] = min(dp[i], dp[j] + 1)
        # return dp[0]
        