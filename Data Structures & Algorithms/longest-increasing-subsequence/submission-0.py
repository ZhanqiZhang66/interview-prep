class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+1)
        dp[n] = nums[-1] + 1

        l = 0

        for i in range(n-1, -1, -1):
            if nums[i] < dp[i+1]:
                dp[i] = nums[i]
                l += 1
            else:
                dp[i] = dp[i+1]
        return l

        