class Solution:

    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]),
                            self.helper(nums[:-1]))
        #only need nums[0] because if we get list that is literally only one house
        #this works 
    def helper(self, nums):
        rob1, rob2 = 0, 0

        for num in nums:
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

        #then same exact algo