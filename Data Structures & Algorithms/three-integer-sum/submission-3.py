class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        def twoSum(nums, target):
            seen = set()
            res = set()
            for i, num in enumerate(nums):
                if target - num in seen:
                    res.add((num, target - num))
                seen.add(num)
            return res

        nums.sort()
        res = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
  
            if nums[i] > 0:
                break
            
            twosum = twoSum(nums[i+1:], -nums[i])
            for pair in twosum:
        
                res.add((nums[i], pair[0], pair[1]))
        return [list(x) for x in res]
        



        