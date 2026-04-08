class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

       # think about i + nums[i]
       #return true if we can reach the end else false if we cant but the
       #thing is we dont need to worry about it that much yet


        max_jump = 0

        for i in range(len(nums)):

            if i > max_jump:  # can't reach this position
                return False
            max_jump = max(max_jump, i + nums[i])
        return True

            
        
        return True