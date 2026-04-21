class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        new_start, new_end = newInterval
        for i in range(len(intervals)):
            start, end = intervals[i]
            if new_end < start:
                res.append(newInterval)
                return res + intervals[i:]
            elif new_start > end:
                res.append([start, end])
            else:
                new_start = min(start, new_start)
                new_end = max(end, new_end)
                newInterval = [new_start, new_end]
        res.append(newInterval)
                
        return res

        