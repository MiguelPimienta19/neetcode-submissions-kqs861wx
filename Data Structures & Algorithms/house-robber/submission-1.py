class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}
        
        def dfs(i):
            if i in memo:
                return memo[i]
            
            if i >= len(nums):
                return 0
            
            res = max(dfs(i + 1), nums[i] + dfs(i + 2))

            memo[i] = res
            return memo[i]
        
        return dfs(0)

        


