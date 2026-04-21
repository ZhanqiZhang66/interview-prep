"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        meetings = defaultdict(int)
        for interval in intervals:
            meetings[interval.start] += 1
            meetings[interval.end] -= 1
        prev = 0
        ans = 0
        for i in sorted(meetings.keys()):
            prev += meetings[i]
            ans = max(ans, prev) # maximum simultaneous meetings.
        return res
        