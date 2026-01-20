"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #sort it by start intervals then iterate over the adjacent items comparing their start and end
        #with lambda, specify what to use for sorting
        sorted_intervals = sorted(intervals, key =lambda x: x.start)

        #now we iter over each comparing start and end if any adjacent conflicts, then it is false
        for i in range(len(sorted_intervals) - 1):
            if sorted_intervals[i+1].start < sorted_intervals[i].end:
                return False
        
        return True
