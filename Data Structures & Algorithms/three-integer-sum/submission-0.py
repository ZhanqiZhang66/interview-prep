class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i]          
            left = i + 1
            right = len(nums) - 1


            while left < right:    
                if nums[left] + nums[right] > -1* target:
                    right -= 1
                elif nums[left] + nums[right] < -1* target:
                    left += 1
                else:
                    ans.append([target, nums[left], nums[right]])
                    left += 1
                    right -= 1  
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return ans         
   
            
            


        