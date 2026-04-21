class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if sum(nums) % 2 > 0 or not nums:
            return False
        target = sum(nums) // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for i in range(n-1, -1, -1):
            for a in range(target, nums[i] -1 , -1):
                dp[a] = dp[a] or dp[a - nums[i]]
        return dp[target]
        
        # dp = [[False] * (target+1) for _ in range(n+1) ]
        # # can first i number used to build target amount
        # for i in range(n+1):
        #     dp[i][0] = True

        # for i in range(n-1, -1, -1):
        #     for a in range(target, 0, -1):
        #         # either nums + previous i can be used to make target - nums[i]
        #         # or previous i cannot be used to make target - nums[i]
        #         # if i don;t use nums[i]
        #         dp[i][a] = dp[i+1][a]
        #         if a >= nums[i]:
        #             dp[i][a] = dp[i][a] or dp[i+1][a - nums[i]]
        # return dp[0][target]



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