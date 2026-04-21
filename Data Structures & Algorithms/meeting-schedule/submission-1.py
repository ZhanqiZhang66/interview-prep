"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i:i.start)
       
        for i in range(1, len(intervals)):
            prev_start, prev_end = intervals[i-1].start, intervals[i-1].end
            start, end = intervals[i].start, intervals[i].end
            if start <= prev_end:
                return False
        return True
