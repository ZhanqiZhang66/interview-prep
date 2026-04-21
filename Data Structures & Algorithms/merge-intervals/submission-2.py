class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(int)
        for start, end in intervals:
            mp[start] += 1
            mp[end] -= 1
        
        res = []
        interval = []
        n_active_intervals = 0 
        for i in sorted(mp):
            if not interval:
                interval.append(i)
            n_active_intervals += mp[i]
            if n_active_intervals == 0:
                interval.append(i)
                res.append(interval)
                interval = []
        return res






        