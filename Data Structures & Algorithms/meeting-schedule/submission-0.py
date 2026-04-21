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
        prev_start, prev_end = intervals[0].start, intervals[0].end
        for interval in intervals[1:]:
            start, end = interval.start, interval.end
            if start <= prev_end:
                return False
        return True
