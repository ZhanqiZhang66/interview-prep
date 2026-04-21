class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = max(nums)
        local_min, local_max = 1, 1

        for n in nums:
            tmp = n * local_min
            local_min = min(n, n * local_min, n * local_max)
            local_max = max(n, tmp, n * local_max)
            
            global_max = max(global_max, local_max)
        return global_max

        