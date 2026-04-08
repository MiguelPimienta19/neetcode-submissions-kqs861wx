class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        #okay we are going to go through the entire list

        #if we ever find a point that it cant keep going we pop it for our stack 
        #and if it can be extended backwards lets do that too. 

        maxarea = 0 
        stack = [] #(index, height)

        for i in range(len(heights)):
            start = i #this is useful to extend backwards if we need

            while stack and stack[-1][-1] > heights[i]: #we can't go on farther. 
                index, height = stack.pop()
                                                #because we had to stop at i, and started at index
                maxarea = max(maxarea, height * (i - index)) 
                start = index #this extends it backwards!!
            
            stack.append((start, heights[i]))
        

        #this is for the ones we have at the end.
        for i, h in stack:
            maxarea = max(maxarea, h * (len(heights) - i))
        
        return maxarea