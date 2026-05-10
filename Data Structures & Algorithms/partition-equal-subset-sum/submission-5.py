class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        n = len(nums)
        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for i in range(n-1, -1, -1):
            for a in range(target, nums[i] - 1, -1):
                dp[a] = dp[a] or dp[a - nums[i]]
        return dp[target]























        # n = len(nums)
        # if sum(nums) % 2 > 0 or not nums:
        #     return False
        # target = sum(nums) // 2

        # dp = [False] * (target + 1)
        # dp[0] = True

        # for i in range(n-1, -1, -1):
        #     for a in range(target, nums[i] -1 , -1):
        #         dp[a] = dp[a] or dp[a - nums[i]]
        # return dp[target]
        
     



        # n = len(nums)
        # if sum(nums) % 2 != 0:
        #     return False
        # target = sum(nums) // 2
        
        # dp = [False] * (target + 1)
        # dp[0] = True

        # for i in range(n-1, -1, -1):
        #     for t in range(target, nums[i]-1, -1):
        #         dp[t] = dp[t] or dp[t - nums[i]]
        # return dp[target]