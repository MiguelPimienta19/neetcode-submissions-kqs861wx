class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        res = 0 
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd: #in rules we say = is fine.
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res


