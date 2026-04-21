class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal_idx = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= goal_idx:
                goal_idx = i
        return goal_idx == 0
        # n = len(nums)
        # dp = [False] * n
        # dp[n-1] = True

        # for i in range(n - 2, -1 , -1):
        #     max_pos = min(n - 1, i + nums[i])
        #     for j in range(i + 1, max_pos + 1):
        #         if dp[j]:
        #             dp[i] = True
        #             break
        # print(dp)
        # return dp[0]
        