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
            print(f"n={n},i={i} ")
            j = 0
            while n + 1 in s and j < len(nums):
                local_max += 1
                j += 1
                n = n + 1
                # print(n)
            
            res = max(res, local_max)
            print(f"n={n},i={i} {res}, {local_max}")
            local_max = 1
            i += 1
        return res
            

        