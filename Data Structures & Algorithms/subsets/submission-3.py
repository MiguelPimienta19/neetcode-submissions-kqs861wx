class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        level = []

        def dfs(i):

            if i >= len(nums):
                res.append(level.copy())
                return 
            
            level.append(nums[i])
            dfs(i + 1)
            level.pop()
            dfs(i + 1)


        dfs(0)

        return res
        