"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # merge overlaps by couting sweeping lines
        if len(intervals) == 1:
            return 1
        sweep = defaultdict(int)
        for interval in intervals:
            start, end = interval.start, interval.end
            sweep[start] += 1
            sweep[end] -= 1
        # depends on > 1 sweeping start , need res += 1
        overlap = 0
        res = 0
        for time in sorted(sweep):
            overlap += sweep[time]
            
            res = max(res, overlap)
        return res


        