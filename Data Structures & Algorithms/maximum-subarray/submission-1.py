class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curmax = 0
    
        for n in nums:
            curmax = max(curmax + n, n)
            res = max(curmax, res)
        return res