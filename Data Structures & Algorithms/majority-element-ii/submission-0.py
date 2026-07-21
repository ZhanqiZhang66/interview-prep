class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
        res = []
        for key in counter:
            if counter[key] > len(nums) // 3:
                res.append(key)
        return res
        