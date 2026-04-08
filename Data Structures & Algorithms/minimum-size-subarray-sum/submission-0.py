class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #since we are trying to return a length we want to use the sliding window tech
        #lets figure out how to do this 

        res = float("inf")
        l = 0

        for r in range(len(nums)):

            while sum(nums[l:r + 1]) >= target and l <= r:
                res = min(res, r - l + 1)
                l += 1
                    
        return 0 if res >= float("inf") else res