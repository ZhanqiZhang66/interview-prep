class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # import bisect
        # return bisect.bisect_left(nums, target)

        l, r = 0, len(nums) 
        #  when mid still >= target, target is the first elemnt
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l

        