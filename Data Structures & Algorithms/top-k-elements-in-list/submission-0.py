class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        c = Counter(nums)
        freq = [key for key, count in c.most_common()]
        return freq[:k]
        