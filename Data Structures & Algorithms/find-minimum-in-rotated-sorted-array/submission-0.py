class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                return nums[mid]
            elif nums[left] < nums[mid] and nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[0]
        