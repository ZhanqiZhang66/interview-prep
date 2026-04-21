class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def backtrack(start, curr):
            ans.append(curr.copy())
            # if len(curr) == start:
            #     ans.append(curr.copy())
            #     return
            for i in range(start, len(nums)):
                if i != start and nums[i] == nums[i-1]:
                    print(f"skip {nums[i]}")
                    continue
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()


        backtrack(0, [])
        return ans
        