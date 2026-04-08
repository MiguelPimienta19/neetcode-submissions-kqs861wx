"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda i: i.start)

        # Compare each pair of neighbors
        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False  # overlap found → cannot attend all
        return True  # no overlaps at all