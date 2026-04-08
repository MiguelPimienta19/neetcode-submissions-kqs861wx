class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        #okay intervals...
        #this one is good we should sort them by the starting points.

        # and when we loop do start, end, hold a prev end variable too??

        #then be like start <= prev end we merger them together??? Im thinking that would be a good idea...
        
        intervals.sort()

        res = [intervals[0]]

        for start, end in intervals: #we are now sorted but start time. 
            
            if res[-1][-1] >= start:
                res[-1][-1] = max(res[-1][-1], end)
            
            else:
            
                res.append([start,end])
        
        return res
