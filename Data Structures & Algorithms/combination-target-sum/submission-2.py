class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        backtrack = []

        def dfs(i, total):

            if total == target:
                res.append(backtrack.copy())
                return #exit and try a new variation. 

            if i >= len(nums) or total > target:
                return #break out of this too.
            
            backtrack.append(nums[i])
            dfs(i, total + nums[i])
            backtrack.pop()

            dfs(i + 1, total)
        
        dfs(0,0)
        return res

