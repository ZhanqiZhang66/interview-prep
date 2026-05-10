class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(i, curr, summ):
            nonlocal res
            if summ == target:
                res.append(curr.copy())
                return
            
            if i < len(nums) and nums[i] + summ <= target:
                curr.append(nums[i])
                backtrack(i, curr, summ + nums[i])
                curr.pop()
                backtrack(i+1, curr, summ)
        backtrack(0, [], 0)
        return res





























        # res = []
        # nums.sort()

        # def backtrack(start, curr, total):    
        #     if total == target:
        #     # if sum(curr) == target:
        #         res.append(curr.copy())
        #         return
        #     for j in range(start, len(nums)):
        #         if total + nums[j] > target:
        #         #if sum(curr) > target: this is O(n)
        #             break
        #         curr.append(nums[j])
        #         backtrack(j, curr, total + nums[j])
        #         curr.pop()
        #     return res
        # backtrack(0, [], 0)
 
        # return res
        