class Solution:
    def trap(self, height: List[int]) -> int:

        res = 0 


        #okay I am going to go to every postion

        #make the min of left and right index i

        #then loop from zero to i to find real min l

        #do the same for right

        #then do min of that minus the current postion we are currently at.


        for i in range(len(height)):
            minleft = height[i]
            minright = height[i]

            for j in range(0, i):
                minleft = max(minleft, height[j])
            
            for j in range(i + 1, len(height)):
                minright = max(minright, height[j])
            
            res += min(minleft, minright) - height[i]
        

        return res