class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = nums[0]
        local_max = nums[0]
        for n in nums[1:]:
            local_max = max(local_max + n, n)
            global_max = max(global_max, local_max)
        return global_max

        