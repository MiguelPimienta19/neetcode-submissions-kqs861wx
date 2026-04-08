class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #since we are trying to return a length we want to use the sliding window tech
        #lets figure out how to do this 

        res = float("inf")
        l = 0
        total = 0

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1  
                    
        return 0 if res >= float("inf") else res