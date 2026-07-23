class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        s = res = 0
        for num in nums:
            s += num
            if s == k:
                res += 1
            if prefix[s - k] > 0:
                res += prefix[s - k]
            prefix[s] += 1
        return res

        