class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            if target - n in d:
                j = d[target - n]
                if i > j:
                    i, j = j, i
                return [i, j]
            d[n] = i
        return [-1, -1]