class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        import bisect
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                idx = bisect.bisect_left(dp, nums[i])
                dp[idx] = nums[i]
        return len(dp)
























        # from bisect import bisect_left
        # dp = []
        # dp.append(nums[0])

        # LIS = 1
        # for i in range(1, len(nums)):
        #     if nums[i] > dp[-1]:
        #         LIS += 1
        #         dp.append(nums[i])
        #     idx = bisect_left(dp, nums[i])
        #     dp[idx] = nums[i]
        # return len(dp)
        