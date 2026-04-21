class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        local_max = 1
        res = 1
        s = set(nums)
        i = 0
        while i < len(nums):
            n = nums[i]
            while n + 1 in s and i < len(nums):
                local_max += 1
                i += 1
                n = n + 1
                print(n)
            res = max(res, local_max)
            local_max = 1
            i += 1
        print(local_max)
        return res
            

        