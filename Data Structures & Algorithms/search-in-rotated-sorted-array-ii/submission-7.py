class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # find first element <= target
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[l] < nums[mid]:
                # left side - mid. is sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < nums[l]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                l += 1
        return False









        # l, r = 0, len(nums) - 1
        # if l == r:
        #     return nums[0] == target
        # while nums[l] == nums[-1]:
        #     l += 1
        #     if l == r:
        #         return nums[l] == target
        # if target <= nums[-1]:
        #     while l < r:
        #         mid = (l + r) // 2
        #         if target <= nums[mid] <= nums[-1]:
        #             r = mid
        #         else:
        #             l = mid + 1
        # else:
        #     while l < r:
        #         mid = (l + r) // 2
        #         if target <= nums[mid] or nums[mid] <= nums[-1]:
        #             r = mid
        #         else:
        #             l = mid + 1
        # return nums[l] == target
        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     mid = (l + r) // 2
        #     if nums[mid] == target:
        #         return True
        #     if nums[mid] > nums[l]:
        #         # on the left side
        #         if nums[l] <= target < nums[mid]:
        #             r = mid - 1
        #         else:
        #             l = mid + 1
        #     elif nums[mid] < nums[l]:
        #         # on the right side
        #         if nums[mid] < target <= nums[r]:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        #     else:
        #         l += 1

        # return False

        