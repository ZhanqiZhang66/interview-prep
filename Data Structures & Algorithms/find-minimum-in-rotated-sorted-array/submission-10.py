class Solution:
    # find which side is not sorted! 
    def findMin(self, nums: List[int]) -> int:
        # find the  num i that < num i - 1, then, this is min
        # so exact search
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
           
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]





























        # find which side is not sorted! 
        # left = 0
        # right = len(nums) - 1

        # while left < right:
        #     mid = (left + right) // 2
        #     if nums[mid] < nums[right]:
        #         right = mid
        #     else:
        #         left = mid + 1
     
        # return nums[left]
        