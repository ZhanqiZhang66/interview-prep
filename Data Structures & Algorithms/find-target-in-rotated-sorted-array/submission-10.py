class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:
                if  nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else: 
                    r = mid - 1
        print(l)
        return -1
         
     




























        # find which side is sorted, search in sorted side
        # l, r = 0, len(nums) - 1
        # while l < r:
        #     mid = (l + r) // 2
        #     if nums[mid] == target:
        #         return mid
        #     # if left side is sorted
        #     if nums[l] <= nums[mid]: # = because l == mid, 1 left case
        #         if  nums[l] <= target < nums[mid]:
        #             r = mid - 1
        #         else:
        #             l = mid + 1 
        #     # if right side is sorted
        #     else :
        #         if nums[mid] < target <= nums[r]: 
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        # return l if nums[l] == target else -1


        