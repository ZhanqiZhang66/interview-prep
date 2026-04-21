class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        INF = float('inf')
        dp = [INF] * n
        dp[n-1] = 0

        for i in range(n - 2, -1, -1):
            jump = nums[i]
            max_jump = min(n - 1, i + jump)
            for j in range(i + 1, max_jump + 1):
                if dp[j] != INF:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[0]
        