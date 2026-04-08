class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # res = []

        # for i in range(len(intervals)):
        #     if newInterval[-1] < intervals[i][0]:
        #         res.append(newInterval)
        #         return res + intervals[i:]
        #     elif newInterval[0] > intervals[i][-1]:
        #         res.append(intervals[i])
        #     else:
        #         newInterval = [
        #             min(newInterval[0], intervals[i][0]),
        #             max(newInterval[-1], intervals[i][-1]),
        #         ]
        # res.append(newInterval)
        # return res

        intervals.append(newInterval)
        intervals.sort()

        res = [intervals[0]]

        for start, end in intervals:
            lastEnd = res[-1][-1]

            if start <= lastEnd:
                res[-1][-1] = max(lastEnd, end)
            else:
                res.append([start, end])
        
        return res
