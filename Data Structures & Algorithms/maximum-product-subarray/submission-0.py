class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp =[float('-inf')] * (n+1)
        dp[n] = 1
        max_p = float('-inf')


        for i in range(n-1, -1 , -1):
            dp[i] = max(dp[i+1] * nums[i], nums[i])
            max_p = max(max_p, dp[i])
        return max_p
        