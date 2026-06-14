class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict, Counter
        res = defaultdict(list)
        for s in strs:
            d = [0] * 26
            for c in s:
                d[ord(c) - ord("a")] += 1
            res[tuple(d)].append(s)
        return list(res.values())

        