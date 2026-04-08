class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        #need to append to this res but we also need to get the end of the first element.



        #we will hold this and if something is greater than this we change the prev end

        # for start, end in intervals:



        # [1, 3] interval [2, 5]

        for i in range(len(intervals)):
            if newInterval[-1] < intervals[i][0]:
                res.append(newInterval) # if our end is less then the start of an interval just add it
                return res + intervals[i:] #we found our merge finish. 
            elif newInterval[0] > intervals[i][-1]: #if our new start is bigger then the current interval we are at
                res.append(intervals[i])
            else:
                newInterval = [ min(newInterval[0], intervals[i][0]), max(newInterval[-1], intervals[i][-1])]
                #this resizes our interval. 
                

        res.append(newInterval)
        return res